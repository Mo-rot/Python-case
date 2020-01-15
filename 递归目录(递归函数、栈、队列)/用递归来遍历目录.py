import os


# 对某个目录里的内容做处理，如果是目录就继续往里打开继续处理，如果是普通文件就对这个文件做读、写或执行处理等

def getDir(path, sp = ""):
    # 得到当前目录下所有的文件
    filesList = os.listdir(path)
    # 处理每一个文件
    sp += "  "
    for fileName in filesList:
        # 判断是否是路劲（用绝对路劲）
        fileAbsPath = os.path.join(path, fileName)
        if os.path.isdir(fileAbsPath):
            # 如果是目录，除了打印还可以做点别的
            print(sp + "目录：", fileName)
            # 这里是递归调用
            getDir(fileAbsPath, sp)
        else:
            # 如果不是目录，除了打印还可以做点别的
            print(sp + "普通文件：", fileName)


getDir(r"C:\Windows")

