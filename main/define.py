import self_edit

def payload_build(inject_param,diction_one):
    inject_param_part=inject_param.split('**')
    if(len(inject_param_part)==0):
                
        payload=diction_one

    elif(inject_param[0]=='*' and len(inject_param_part)==2):
        payload=diction_one + inject_param_part[1]

    elif(inject_param[len(inject_param)-1]=='*' and len(inject_param_part)==2):
        payload=inject_param_part[1] + diction_one

    elif(len(inject_param_part)==3):
        payload=inject_param_part[0] + diction_one + inject_param_part[2]
    return payload
#用于整理装载语句




def is_my_payload(payload,is_on):
    if(is_on=="on"):
         return self_edit.my_payload(payload)
    else:
        return payload
#判断是否加载自己的脚本