#Write a function 'zip_list', that takes two lists, of the same length,
#and returns a single list, where each element is a tuple containing
#elements from the same position in each list.

#solution
def zip_list(list1, list2):
    pair = list(zip(list1, list2))#Use the zip function
    return pair
#Test
list1 = [32, 12, 34, 56, 23]
list2 = [11, 12, 23, 33, 76]
print(zip_list(list1, list2))