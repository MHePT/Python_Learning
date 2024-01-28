# print(111_111_111)
# print(0o123)
# print(0x123)
# name = input("Enter your Name: ")
# print("My","Name","is",name,sep=",",end=".\n")
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))         #CTRL + K to comment multi-lines
 
# # Choose the larger number
# if number1 > number2: larger_number = number1
# else: larger_number = number2

# for i in range(100):
#     pass
# while number1:
#     pass
#     print("test")
#     number = 0

numbers = [10, 5, 7, 2, 1]
print("Original list contents:", numbers)  # Printing original list contents.

numbers[0] = 111
print("New list contents: ", numbers)  # Current list contents.

del numbers[-1]
print("Length of list After Deletion last member: ", len(numbers))
print("New list contents: ", numbers)

numbers.append(100)
numbers.insert(1,222)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
print()

for num in numbers:
    print(num)

print()

#Be Aware that Python not copys but Points to same list
list_1 = [1]
list_2 = list_1    # Points to the same object
list_1[0] = 2
print(list_2)      # output = 2

#Now Python copys
list_1 = [1]
list_2 = list_1[:] # Copy of the object list[start:end] end not included
list_1[0] = 2
print(list_2)      # output = 1

del list_1
del list_2

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]
print(new_list)     # output = [8,6]

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:-2]
print(new_list)     # output = [8,6]

my_list = [10, 8, 6, 4, 2]
new_list = my_list[-1:1]
print(new_list)     # output = []

my_list = [10, 8, 6, 4, 2]
del my_list[1:3]
print(my_list)      # output = [10, 4, 2]

print(5 in my_list)
print(5 not in my_list)
print(10 in my_list)

temps = [[0.0 for h in range(24) if True] for d in range(31)] # 24x31 Matrix 
