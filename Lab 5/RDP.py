

def S():
	if string[i] = "(":
		print(string + "S → (L)")
		i+=1
		if (L()):
			if (string[i] == ")"):
				i+=1
				return 1
			else:
				return 0
		else:
			return 0
	else if string[i] = "i":
		i+=1
		print(string + "S →a")
