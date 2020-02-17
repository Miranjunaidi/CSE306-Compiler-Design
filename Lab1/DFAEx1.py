def transition (Q,S):
	if Q == 0 and S == "a":
		return 1
	if Q == 0 and S == "b":
		return 3
	if Q == 1 and S == "a":
		return 0
	if Q == 1 and S == "b":
		return 2
	if Q == 2 and S == "a":
		return 3
	if Q == 2 and S == "b":
		return 1
	if Q == 3 and S == "a":
		return 2
	if Q == 3 and S == "b":
		return 0

string = input("Enter the string in a and b to check")
Q = 0
for i in string:
	Q = transition(Q,i)
#print(Q)

if Q == 0:
	print("Accepted")
else:
	print("Rejected")
