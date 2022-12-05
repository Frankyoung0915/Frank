"""用python设计第一个游戏"""
import random
answer = random.randint(1,10)

counts = 3

while counts >0:
   temp = input("不妨猜一下心里现在所想的数字")
   guess = int(temp)

   if guess == answer:
    print("你是我心里的蛔虫吗")
    print("11")
    break

   else:
      if guess < answer:
        print("小啦")
      else:
        print("大啦")
   counts = counts - 1

print("game over")