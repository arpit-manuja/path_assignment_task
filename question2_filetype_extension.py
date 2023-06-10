def file_types(e_t_string, file_list):
    extension_type = e_t_string.split(';')
    e_t_dict = {}
    for pair in extension_type:
        extension, file_type = pair.split(',')
        e_t_dict[extension] = file_type

    result_dict = {}
    for file in file_list:
        extension = file.split('.')[-1]
        file_type = e_t_dict.get(extension, 'unknown')
        result_dict[file] = file_type

    return result_dict



input_string = input("Enter input string in format extension:type;.. ")
list1=[]
n = int(input("Enter number of file.extension you want to enter in list"))
for i in range(n):
    element = input("Enter file.extension element in list")
    list1.append(element)


result = file_types(input_string, list1)
print(result)

