
# This function is irrelavant and did not use 
def pop (stack_string , num):
	return stack_string[:-num]

# Shifts from inpot to stack
def shift (stack_string , Our_string):
	stack_string += Our_string[0]
	Our_string = Our_string[1:]
	return stack_string , Our_string

#Checks the top of the stack for a handle
def is_handle(stack_string,grammar):
	for i in grammar:
			if len(stack_string) >= len(i) and i == stack_string[-len(i):]:
				stack_string = stack_string[:-len(i)] + "S"
				print("S ->" , i)
	return stack_string

# Given Grammar
# S -> 0S0 | 1S1 | 2

grammar = ["0S0","1S1", "2"]

# Concidered String = 0102010 (Belongs to the given grammar)

stack_string = "$"
Our_string = "0102010$"
rules = []

for i in range(len(Our_string)):
	stack_string , Our_string =  shift(stack_string , Our_string )
	stack_string = is_handle(stack_string , grammar)
	#print(stack_string)

# is_handle("$1S1" , grammar)
