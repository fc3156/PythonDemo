number = 23
running = True
while running:
    guess = int(input('Enter an integer:'))
    if guess == number:
        print('Congratulations,you guessed it.')
        # 这将導致while循环结束
        running = False
    elif guess < number:
        print('No,it is a little higher than that.')
    else:
        print('No,it is a little lower than that.')
else:
    print('The while loop is over.')
    #在这里可以做想做事。。。
print('Done')
