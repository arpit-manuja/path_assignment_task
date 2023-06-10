def f(x , l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
# Output is [0,1]
#In this we are passing the only one argument 2 and list premade in function is [] 
# so value 0*0 and 1*1 will be put in list and final list will [0 , 1]

f(3 , [3 ,2 ,1])
# Output is [3 ,2 ,1 ,0 , 1, 4]
#In this we are passing the two argument 3 and list = [3 ,2 , 1] 
#so value 0*0 and 1*1  and 2*2 will be put in list and final list will be [3 ,2 , 1, 0 , 1, 4]

f(3)
# output is [0 ,1 , 0 ,1 , 4]
#In this we are passing only one argument and list = []
#Now main point is initial list will not be empty it will have [0 , 1] because in f(2) no list is passed
#so f(3) will used that list only which was [0 , 1]
# so value 0*0 , 1*1 and 2*2 will be put in list and final list will be [0 , 1, 0 ,1 , 4]





