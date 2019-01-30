# -- coding: utf-8 --
import random

number = random.randint(0,9)
running = True

while running:
    guess = int(input('Enter an integer : '))

    if guess == number:
        print('Congratulations, you guessed it.')
        # 这会导致 while 循环停止
        running = False

    elif guess < number:
              print('小了')
    else:
             print('大了')


else:
         print('The while loop is over.')
    # 你可以在此处继续进行其它你想做的操作

print('Done')