
def fun(inputList , key_input):
    outputList = sorted(inputList , key = lambda x:x[key_input])
    return outputList


inputList = []

n = int(input("Enter number of dictionaries you want to enter in List"))
num = int(input("Enter key value pair you want to enter in each dictionary"))

for i in range(n):
    dictionary = {}
    print("Enter  key value in new dictionary")
    for j in range(num):
       
        key = input("Enter key ")
        value = input("Enter value")
        dictionary[key] = value
    inputList.append(dictionary)

print("input list " , inputList);


key_input = input("Enter key by which you want to sort")

outputList = fun(inputList ,key_input )

print("output list ", outputList);



       
   
    
