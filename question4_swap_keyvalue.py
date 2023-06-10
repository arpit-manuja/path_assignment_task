
#key_value_swap_function

def swap_function(inputDictionary):
    output_dictionary = {value : key for key , value in inputDictionary.items()}
    return output_dictionary
    



inputDictionary = {}

n = int(input("Enter the Key value You want to enter in dictionary "))

for i in range(n):
    key = input("Enter key ")
    value = input("Enter value ")
    
    inputDictionary[key] = value
    
print("Input dictionary    ",inputDictionary)

switch_Key_Value_dict = swap_function(inputDictionary)


print("output dictionary  ",switch_Key_Value_dict)

