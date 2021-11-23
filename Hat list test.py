hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

#line of code that prompts the user
#replace the middle number with an integer number entered by the user.
hat_list[2] = int(input('Please enter the third number '))
#removes the last element from the list.
del hat_list[4]
#prints the length of the existing list.
print("\nNew list content:", hat_list)

print(hat_list)
