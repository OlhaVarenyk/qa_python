# var = 'friend'
# message = 'Hello, '+ var
# print(message)
# helloworld = "hello" + " " + "world"
# print(helloworld)



# a = input('Ваша попередня вага: ')
# b = input('Ваша сьогоднішня вага: ')
# if b > a:
#   print("Ви набрали вагу.")
# elif a == b:
#   print("Без змін.")
# else:
#   print("Ви втратили вагу.")

import random
randomlist = []
for i in range(0,10):
  n = random.randint(1,30)
  randomlist.append(n)
print(randomlist)
odd = []
even = []
for number in randomlist:
  if number%2==0:
    even.append(number)
  else:
    odd.append(number)

print(even)
print(odd)