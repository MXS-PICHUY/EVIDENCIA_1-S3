import random
mylist = ['apple','banana','cherry']
print(random.choice(mylist, weights=[10,1,1],k=14))