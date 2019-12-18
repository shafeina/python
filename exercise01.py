"""
    练习：编写一个程序,向一个文件中不断写入如下内容：

        1.2019-1-1  18:18:18
        2.2019-1-1  18:18:20
        3.2019-1-1  18:18:22
        4.2019-1-1  18:18:24

    每次写入占一行
    这是一个死循环，2s写入一次，但是可以实时查看写入内容
    当程序退出，重新启动后，书写内容能够衔接之前序号内容
"""
# import time
# f = open("file_time","a+")
# f.seek(0)
# n = 1
# for i in f:
#     n += 1
# while True:
#     time.sleep(2)
#     tuple_time = time.localtime()
#     i = time.strftime("%Y-%m-%d %H：%M：%S", tuple_time)
#     o = "%d,%s\n"%(n,i)
#     f.write(o)
#     f.flush()
#     n += 1

