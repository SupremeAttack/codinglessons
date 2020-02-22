#the for loop

alex_is_ithe_best = True
age = 15

while (alex_is_ithe_best is True):
    print("yes its true")
    alex_is_ithe_best = False


size = 99
while (age < 50): # chile age is under 50
    #do this
    print(age)
    while(size < 100):
        size = size - 1
        print ("size "+ str(size))
        size = size + 1000
    age = age +1



#Lists

myNumbers = [4, 7, 22]

for i in myNumbers:
    print(i)

allnumtocent = range(100)
for i in range(100): # for(var i = 0 ; i< 99; i=i+1)
    print(i)

#Write the above loop with a while loop

number=0
while (number < 100):
    print (number)
    number = number + 1


# conditions and boolean expression

# and, or, is , not
# &&, ||, ==, !=
age = 15
if(age < 18):
    print("too young!!")
else:
    print("ok!!")

# use loop , if and modulo operator to print all the odd numbers
"""
1
3
5
7
9
11
...
99
"""
numbers = range(100)
"""
number=1
while (number<10000000)
print (number)
number= number+2
if number>10000000
"""
#for i in range(100):#

def isOdd(n):
    return n % 2


for i in numbers:
    if(isOdd(i)):
        print(i)
    



