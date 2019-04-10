# StartTime: 2019.04.10
# auther: Leo

# code can change world

# idea: Updateable, Expandable
# 理念
# 发现一种密码组合形式就记录下来，不断填充，达到精准匹配密码的目标

# 欢迎
def welcome():
    print("---------------Welcome to Leo's world---------------")

# 进行组合并输出

# 0. 将top100的密码加入输出
def base_secret():
    f = open("../attach/top100.txt")
    read_secrets = f.read()
    f.close()
    fw = open("../output/pwd.txt", "w")
    fw.write(read_secrets)
    fw.close()


# 1. 姓和座机号的组合
def secret_combination_1(name_first, land_phone):
    secret_1 = name_first + land_phone
    secret_2 = land_phone + name_first
    secret = '\n' + secret_1 + '\n' + secret_2
    fa = open("../output/pwd.txt", "a")
    fa.write(secret)


# 执行
welcome()
# name_short = input("please input chinese short name: ")
name_first = input("please input chinese first name: ")
# name_last = input("please input chinese last name: ")
# name_english = input("please input english name: ")
# username = input("please input username: ")
# phone = input("please input phone: ")
land_phone = input("please input landline phone: ")
# qq = input("please input qq number: ")
# date_birth = input("please input birth date: ")
# lover_name_short = input("please input lovers chinese short name: ")
# lover_name_first = input("please input lovers chinese first name: ")
# lover_name_last = input("please input lovers chinese last name: ")
# string_special = input("please input special string: ")
base_secret()
secret_combination_1(name_first, land_phone)