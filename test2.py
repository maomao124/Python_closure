"""
 * Project name(项目名称)：Python闭包
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 14:29
 * Version(版本): 1.0
 * Description(描述)： 
 """


# 闭包函数，其中 exponent 称为自由变量
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of  # 返回值是 exponent_of 函数


if __name__ == '__main__':
    square = nth_power(2)  # 计算一个数的平方
    cube = nth_power(3)  # 计算一个数的立方
    print(square(2))  # 计算 2 的平方
    print(cube(2))  # 计算 2 的立方
    # 闭包比普通的函数多了一个 __closure__ 属性，该属性记录着自由变量的地址。当闭包被调用时，系统就会根据该地址找到对应的自由变量，完成整体的函数调用。
    print(square.__closure__)
