import re
class analys:
    def __init__(self,allresponse):
        self.allresponse=allresponse
    #

    def key_find(self):
        keys1=[] 
        for key,value in self.allresponse.items():
            matches=re.findall(key,value)
            if(matches):
                keys1.append(key)
            else:
                continue
        return keys1
    #查找键名是否存在于值中


    def error_find(self):
        keys2=[]
        for key,value in self.allresponse.items():
            new_value=value.upper()
            matches=re.findall('ERROR',new_value)
            if(matches):
                keys2.append(key)
            else:
                continue
        return keys2
    #查找值中是否有error元素


    def len_find(self,ilen):
        keys3_up=[]
        keys3_lower=[]
        for key,value in self.allresponse.items():
            if(len(value)>=ilen):
                keys3_up.append(key)
            else:
                keys3_lower.append(key)
        return keys3_up
    #长度判断


    def my_find(self,param):
        keys4=[]
        for key,value in self.allresponse.items():
            matches=re.findall(param,value)
            if(matches):
                keys4.append(key)
            else:
                continue
        return keys4
    #自定义查找

#
def analysis(allresponse):
    objectt=analys(allresponse)
    while(1):
        print("执行操作：")
        print("1 for 长度查找")
        print("2 for 键值查找")
        print("3 for error查找")
        print("4 for 自定义查找查找")
        print("0 for exit")
        choose=input()
        if(choose=='1'):
            print("输入长度：")
            choose=input()
            try:
                keys=analys.len_find(objectt,choose)
                print("长度大于该值的键值：")
                print(keys)
            except:
                print("输入有误或未找到")

        elif(choose=='2'):
            keys=analys.key_find(objectt)
            print("值中存在键的有：" )
            print(keys)

        elif(choose=='3'):
             keys=analys.error_find(objectt)
             print(keys)

        elif(choose=='4'):
            print("输入要查找的内容：")
            valuee=input()
            keys=analys.my_find(objectt,valuee)
            print("查找结果：")
            print(keys)

        elif(choose=='0'):
            break
        else:
            print("输入不正确！")
    return 0
#a={'1':"123456",'w':"qsddd",'error':"qwweeeeeerror"}
#analysis(a)

