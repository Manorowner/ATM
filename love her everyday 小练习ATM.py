money=5000000
name=input('请输入你的姓名:')
def ATM(aaaaa):
    if aaaaa:
        print(f"{name},你好,欢迎来到黑马银行ATM.请选择操作:                                              ")
        print('查询金额\t[输入1]')
        print('存款\t\t[输入2]')
        print('取款\t\t[输入3]')
        print('退出\t\t[输入4]')
        return input('请输入你的选择:')#将input返回出去
    return input('请输入4用以退出:')
def b(aaa):
    if aaa:
        print('------------------------------查询金额------------------------------')
    print(f'{name},你好,你的余额剩下:{money}元.')
def c(qian):
    print('------------------------------存款----------------------------------------')
    global money
    money+=qian
    print(f'{name},你好,你成功存入{qian}元')
    b(False)
def d(qian):
    print('------------------------------取款-----------------------------------------------')
    global money
    money-=qian
    if money>=0:
        print(f'{name},你好,你成功取走{qian}元')
        b(False)
    else:
        money+=qian
        print('你的余额不足')
while True:
    sss=ATM(True)#sss给input做变量
    if sss=="1":
        b(True)
        ATM(False)
    elif sss=="2":
        qian=int(input("你要存入多少钱:"))
        c(qian)
        ATM(False)
    elif sss=="3":
        qian=int(input('你要取走多少钱:'))
        d(qian)
        ATM(False)
    elif sss=="4":
        ATM(True)













