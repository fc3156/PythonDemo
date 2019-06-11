number = 23
guess = int(input('input a integer:'))
if guess == number:
    #新語句塊從這裏開始，注意if后面的冒号
    print('congratuations,you guess it!')
    # 新語句塊在這裏結束
elif guess < number:
    #另外一個代碼塊
    print('No,it is a little higher than that..')
    #另外代码块结束
else:
    print('No,it is a little low than that...')

    print('Done')
