A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print(A0)

#it will print {'a':1 , 'b':2 , 'c':3 , 'd':4 , 'e':5} 
#because dict keyword convert it in dictionart and zip keyword combine two tuples so first tuple will
#be key and second tuple will be value

A1 = range(10)
print(A1)

#It will print range(0 , 10)
# 0 , 1, 2,3,4 ,5,6, 7, 8 , 9 will not print it will print when we convert A1 into list 

A2 = sorted([i for i in A1 if i in A0])
print(A2)

#it will print [] empty list
#because there are numbers stored in A1 from 0 to 9 but in A0 keys are a , b , c, d, e 
#so we have to sort  that values which is in A1 also in A0 but nothin is there

A3 = sorted([A0[s] for s in A0])
print(A3)

#it will print [1,2,3,4,5]
#because A0 has keys a, b , c, d,e  and their values are 1,2,3,4,5

A4 = [i for i in A1 if i in A3]
print(A4)

#it will print [1,2 ,3,4,5]
#because A1 has 0 , 1,2,3,4,5,6,7,8,9 and A3 has 1,2,3,4,5 
#so we have to tarverse A1 and store in list which also in A3  which are 1,2 ,3 ,4,5

A5 = {i:i*i for i in A1}
print(A5)

#it will print {0:0 , 1:1 , 2:4 , 3:9 , 4:16 , 5:25 , 6:36 , 7:49 , 8:64 , 9 :81}
#because A1 has 0 to 9 elements and in this we can see curly barckets so this is dictionary 
# key is 0 to 9 and values are squares of 0 to 9

A6 = [[i,i*i] for i in A1]
print(A6)

#it will print [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]
#becuase it is same as A5 but instead of dictionary it using list . nested lists instead

from functools import reduce
A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
print(A7)

#it will print 21
#because it will add 10 + 23 -45 + 33 as it using reduce which convert whole iteration into single variable
#and lambda is used for making function stuff clear and easy to use and 
#for using reduce we have to import reduce from functools

A8 = map(lambda x: x*2, [1,2,3,4])
print(A8)

#basically it will print  <map object at 0x000001F59AADB010>  and [2 ,4 , 6,8]
#but i we do some changes because there is not any container in which we are storing
#if we print it in list i
print("extended A8" , list(A8))


A9 = filter(lambda x: len(x) >3, ["I", "want", "to", "learn", "python"])
print(A9)

#['want ' , 'learn' , 'python']
#it will filter that strings which has length greater than 3
#when we store it in conatiner then

print(list(A9))





