# 爱奇艺第66_06:45_用队列模拟递归来遍历目录(广度遍历)

import os
import collections


def getDir_GuangDu(path):
    queue01 = collections.deque()
    # 进队
    queue01.append(path)

    while len(queue01) != 0:
        # 出对数据
        dirPath = queue01.popleft()
        # 找出所有的文件
        filesList = os.listdir(dirPath)

        for fileName in filesList:
            # 绝对路径
            fileAbsPath = os.path.join(dirPath, fileName)
            # 判断是否是目录，是目录就进队，不是就打印
            if os.path.isdir(fileAbsPath):
                print("目录：" + fileName)
                queue01.append(fileAbsPath)
            else:
                print("非目录：" + fileName)


getDir_GuangDu(r"C:\Windows")

