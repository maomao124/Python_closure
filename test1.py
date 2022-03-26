"""
 * Project name(项目名称)：Python闭包
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 14:06
 * Version(版本): 1.0
 * Description(描述)： 杀掉酷狗音乐偷上传流量进程
 """
import os
import time

if __name__ == '__main__':
    while 1:
        cmd = "taskKill /f /t /im KGService.exe"
        os.system(cmd)
        time.sleep(0.5)
