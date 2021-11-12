import random

com = random.randint(1,100)
print('電腦選擇之號碼為:',com)

min = 1
max = 100
while True:
    me = int(input('請輸入%d~%d之數字:' %(min,max)))
    if com == me:
        print('您猜對了!!')
        break
    elif com < me:
        max = me
    else:
        min = me