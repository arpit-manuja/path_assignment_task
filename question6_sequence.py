
def findsequence(inputList , starting_index , ending_index):
    output_list = []
    for i in range(starting_index  , ending_index+1 , 2):
        output_list.append(inputList[i])
    return output_list
    


n = int(input("Enter  number of element you want to enter in List  "));

inputList = [];
for i in range(n):
    num = int(input("Enter element"));
    inputList.append(num);

starting_index = int(input("Enter the Starting index  "))
ending_index = int(input("Enter the ending index"))


output_list = findsequence(inputList , starting_index , ending_index);

print("input list is " , inputList)
print("output list is " ,output_list)

    
