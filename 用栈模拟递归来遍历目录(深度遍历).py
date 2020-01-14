import os


def getDirDepth(path):
    stack01 = []
    stack01.append(path)

    # 处理栈，当栈为空时结束循环
    while len(stack01) != 0:
        # 从栈里取出数据
        dirPath = stack01.pop()
        # 目录下所有文件
        filesList = os.listdir(dirPath)
        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath, fileName)
            # 判断是否是目录，是就压栈，不是就打印
            if os.path.isdir(fileAbsPath):
                print("目录：" + fileName)
                stack01.append(fileAbsPath)
            else:
                print("非目录：" + fileName)





getDirDepth(r"C:\Windows")







