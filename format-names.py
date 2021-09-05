#Write a function, 'format-names', that takes a list of names,
#and returns the names properly formatted.
#i.e each name will start with capital letter.

#Solution

def format_names(names):
    return [name.capitalize() for name in names]

names = ['dog', 'fiSH', 'cat', 'TIGER', 'RaBBiT']
print(format_names(names))