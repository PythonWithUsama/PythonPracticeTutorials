'''
list comprehension
here list1 is list variable
here iter is a loop variable
'''
# list1 = [iter for iter in range(1,11) if iter%3==0]
# print(list1)
'''
dictionary comprehension
here dict1 is dictionary variable.
here dict_key is dictionary key and also loop variable
'''
# dict1 = {dict_key:f"item {dict_key}" for dict_key in range(1,50) if dict_key%10==0}
# print(dict1)
'''
comprehension method to reverse the dictionary
here dict2 is new dictionary variable...
here value:key for key,value in dict1.items() == value=key and key=value ky.. for reverse method
'''
# dict2 = {value:key for key,value in dict1.items()}
# print(dict2)

'''
here dressess is class set variable and dress is a loop variable
to find the class dressess varibales print(type(dressess))
'''
dressess = {dress for dress in ["black","blue","black","white","gray","white"]}
print(dressess)
print(type(dressess))
