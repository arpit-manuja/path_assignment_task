

# selectionSort function given below---

def selectionSort(inputList):
    n = len(inputList)
    for i in range(0 , n-1):
        minn = inputList[i]
        index = i
        for j in range(i+1 , n):
            if inputList[j]<minn:
                minn = inputList[j]
                index = j
        inputList[i] , inputList[index] = inputList[index], inputList[i]
    
    return inputList

# input-----

n = int(input("Enter number of elements you want to put in list  "))

inputList = []

for i in range(n):
    x = int(input("Enter element "))
    inputList.append(x)

print("input list is :->" ,  inputList)


sortedList = selectionSort(inputList)
print(" list after sorting:->" , sortedList)


            
        
    
