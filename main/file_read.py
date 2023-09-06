#
def conf_read(file_path):
    parameters={}
    with open(file_path,'r') as file:
        for line in file:
            line=line.strip()
            #逐行读取文件
            if line:
                paramAndvalue=[]
                paramAndvalue=line.split('==')
                param=paramAndvalue[0]
                value=paramAndvalue[1]
                parameters[param.strip()]=value
    return parameters
#
def dic_read(file_path):
    dict_list=[]
    i=0
    with open(file_path,'r') as file:
        for line in file:
            line=line.strip()
            if line:
                dict_list.append(line)
                i=i+1
    return dict_list