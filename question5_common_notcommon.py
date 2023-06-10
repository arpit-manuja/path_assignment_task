def fun(list1 , list2):
    common = list(set(list1) & set(list2))
    not_common = list(set(list1)^ set(list2))
    
    return common , not_common;

list1 = []
list2 = []

num1 = int(input('Enter elements you want to put in list1'))
for i in range(num1):
    elements = input("Enter element of list1")
    list1.append(elements)
    
num2 = int(input('Enter elements you want to put in list2'))
for i in range(num2):
    elements = input("Enter element of list2")
    list2.append(elements)
    
common , not_common = fun(list1  , list2)

print("Common elements are " , common)
print("not common elements are" , not_common)
