def pop (stack_string , num):
	return stack_string[:-num]

def shift (stack_string , Our_string):
	stack_string += Our_string[0]
	Our_string = Our_string[1:]
	return stack_string , Our_string

def is_handle(stack_string,grammar):
	for i in grammar:
			if len(stack_string) >= len(i) and i == stack_string[-len(i):]:
				stack_string = stack_string[:-len(i)] + "S"
				print("S ->" , i)
	return stack_string


grammar = ["0S0","1S1", "2"]

stack_string = "$"
Our_string = "0102010$"
rules = []

for i in range(len(Our_string)):
	stack_string , Our_string =  shift(stack_string , Our_string )
	stack_string = is_handle(stack_string , grammar)
	#print(stack_string)

# is_handle("$1S1" , grammar)
