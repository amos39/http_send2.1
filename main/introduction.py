def introd():
    try:
    
        with open('./READ_ME.md','r',encoding='utf-8') as file:
            print(file.read())
            print("如果你想启动时关闭此介绍，可更改配置文件中的introduction选项")
    except:
        print("README文件不存在！")
    return 0