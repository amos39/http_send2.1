import file_read as read
import introduction
import judge
import define
import http_analysis

import requests
import time
#

try:
    conf=read.conf_read('./conf.txt')
except:
    print("配置文件打开错误！")
    exit()
#
try:

    diction_list=(conf['dictionary'].strip()).split(';')
    #print(diction_list)
    dict_path_part="./dictionary/"
    diction=[]

    for i in range(len(diction_list)):
        dic_path=dict_path_part + diction_list[i]
        diction=read.dic_read(dic_path)
        diction.extend(diction)
except:
    print("字典加载有误！")
    exit()

if(not(conf['introduction']=="off")):
    introduction.introd()

print(("------------------------------------------------------------------------------------"))
print("欢迎使用自助发包脚本(http_send)2.1")
print("author by amos")
print(("------------------------------------------------------------------------------------"))

if(conf['delay-time']=="" or conf['for-time']=="" or conf['url']==""):
    print("必要参数未设置！")
    exit()

print("测试url:"+conf['url'])
try:
    r=requests.get(conf['url'],timeout=7)
    #print(r.text)
except:
    print("url连接失败或响应超时")
    exit()
print("连接成功！")

##进行系列配置测试
with open('./conf.txt') as confo:
    print("当前配置：")
    print(confo.read())

allresponse={}
header={'user-agent':conf['user-agent']}
#全局默认变量

if(conf['method'].lower()=="get"):
    if(conf['inject-position']=="url"):
        print("请输入参数，并在需要注入的参数位置的两边加上**")
        inject_param=input()
        inject_param_part=inject_param.split('**')

        for i in range(len(diction)):
            if(len(inject_param_part)==1 or len(inject_param_part)==0):
                print("输入有误！")
                exit()

            elif(len(inject_param_part)==2):
                payload=conf['url'] + '?' + inject_param_part[0] + diction[i]

            elif(len(inject_param_part)==3):
                payload=conf['url'] + '?' + inject_param_part[0] + diction[i] + inject_param_part[2]
            payload=define.is_my_payload(payload,conf['my_payload'])
            r=requests.get(payload,cookies=conf['cookie'],headers=header,timeout=float(conf['delay-time']))
            
            print(payload)
            allresponse[diction[i]]=r.text
            time.sleep(float(conf['for-time']))


    elif(conf['inject-position']=="user-agent"):
         print("请输入一个user-agent并用**包括替换位置")
         inject_param=input()
         inject_param_part=inject_param.split('**')

         for i in range(len(diction)):
            if(len(inject_param_part)==0):
                uaheader={'user-agent':diction[i]}
                payload=define.is_my_payload(uaheader['user-agent'],conf['my_payload'])
                uaheader={'user-agent':payload}
                r=requests.get(conf['url'],cookies=conf['cookie'],headers=uaheader,timeout=float(conf['delay-time']))

            elif(inject_param[0]=='*' and len(inject_param_part)==2):
                uaheader={'user-agent':diction[i] + inject_param_part[1]}
                payload=define.is_my_payload(uaheader['user-agent'],conf['my_payload'])
                uaheader={'user-agent':payload}
                r=requests.get(conf['url'],cookies=conf['cookie'],headers=uaheader,timeout=float(conf['delay-time']))

            elif(inject_param[len(inject_param)-1]=='*' and len(inject_param_part)==2):
                uaheader={'user-agent':inject_param_part[1] + diction[i]}
                payload=define.is_my_payload(uaheader['user-agent'],conf['my_payload'])
                uaheader={'user-agent':payload}
                r=requests.get(conf['url'],cookies=conf['cookie'],headers=uaheader,timeout=float(conf['delay-time']))

            elif(len(inject_param_part)==3):
                uaheader={'user-agent':inject_param_part[0] + diction[i] + inject_param_part[2]}
                payload=define.is_my_payload(uaheader['user-agent'],conf['my_payload'])
                uaheader={'user-agent':payload}
                r=requests.get(conf['url'],cookies=conf['cookie'],headers=uaheader,timeout=float(conf['delay-time']))

            print(uaheader['user-agent'])
            allresponse[diction[i]]=r.text
            time.sleep(float(conf['for-time']))


    elif(conf['inject-position']=="cookie"):
         print("请输入样例cookie，并在需要注入的位置的两边加上**")
         inject_param=input()
         inject_param_part=inject_param.split('**')

         for i in range(len(diction)):
            if(len(inject_param_part)==0):
                payload_cookie=diction[i]

            elif(inject_param[0]=='*' and len(inject_param_part)==2):
                payload_cookie=diction[i] + inject_param_part[1]

            elif(inject_param[len(inject_param)-1]=='*' and len(inject_param_part)==2):
                payload_cookie=inject_param_part[1] + diction[i]

            elif(len(inject_param_part)==3):
                payload_cookie=inject_param_part[0] + diction[i] + inject_param_part[2]

            payload=define.is_my_payload(payload_cookie,conf['my_payload'])
            r=requests.get(conf['url'],cookies=payload,headers=header,timeout=float(conf['delay-time']))
            print(payload_cookie)
            
            allresponse[diction[i]]=r.text
            time.sleep(float(conf['for-time']))


    else:
        print("inject-position不支持！")
        exit()

elif(conf['method'].lower()=="post"):
    if(conf['inject-position']=="url"):
        print("post模式不允许inject-position参数")
        exit()

    elif(conf['inject-position']=="body"):
         print("请输入参数，并在需要注入的参数的两边加上**")
         inject_param=input()
         for i in range(len(diction)):
            payload=define.payload_build(inject_param,diction[i])
            payload=define.is_my_payload(payload,conf['my_payload'])
            r=requests.post(conf['url'],headers=header,cookies=conf['cookie'],data=payload,timeout=float(conf['delay-time']))
            
            print(payload)
            allresponse[diction[i]]=r.text
            time.sleep(float(conf['for-time']))
    
    elif(conf['inject-position']=="user-agent"):
         print("请输入参数，并在需要注入的参数的两边加上**")
         inject_param=input()
         for i in range(len(diction)):
            payload=define.payload_build(inject_param,diction[i])
            uaheader={'user-agent':payload}
            payload=define.is_my_payload(uaheader['user-agent'],conf['my_payload'])
            uaheader={'user-agent':payload}
            r=requests.post(conf['url'],headers=uaheader,cookies=conf['cookie'],data=conf['post-body'],timeout=float(conf['delay-time']))
            
            allresponse[diction[i]]=r.text
            print(payload)
            time.sleep(float(conf['for-time']))

    elif(conf['inject-position']=="cookie"):
         print("请输入参数，并在需要注入的参数的两边加上**")
         inject_param=input()
         for i in range(len(diction)):
            payload=define.payload_build(inject_param,diction[i])
            payload=define.is_my_payload(payload,conf['my_payload'])
            r=requests.post(conf['url'],headers=header,cookies=payload,data=conf['post-body'],timeout=float(conf['delay-time']))
            
            print(payload)
            allresponse[diction[i]]=r.text
            time.sleep(float(conf['for-time']))

    else:
        print("inject-position参数不支持！")
        exit()

else:
    print("不支持的method")
    exit()

end_output=judge.classify_dict_values(allresponse)
for key,value in end_output.items():
    print(key,value)


print("是否加载分析模块？（y/n）")
choose=input()
if(choose=="y"):
    print()
    http_analysis.analysis(allresponse)

elif(choose=="n"):
    exit()

else:
    print("输入有误！")
    exit()