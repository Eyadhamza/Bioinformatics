# file handling

# 1) without using with statement
file = open('file_path', 'w')
file.write('filename !')
file.close()

# 2) without using with statement
file = open('file_path', 'w')
try:
    file.write('filename')
finally:
    file.close()

# using with statement
with open('file_path', 'w') as file:
    file.write('filename !')
