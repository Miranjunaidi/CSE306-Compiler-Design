from automata.fa.dfa import DFA

Machine = DFA(
	states = {"0","1","2","3"},
	input_symbols = {'a','b'},
	transitions = { "0": { "a":"1" , "b":"3" },
				   "1": { "a":"0" , "b":"2" },
				   "2": { "a":"3" , "b":"1" },
				   "3": { "a":"2" , "b":"0" } },
	initial_state="0",
	final_states={"0"}  
)
string = input("Enter the input you want to recognise")
if Machine.accepts_input(string):
    print('accepted')
else:
    print('rejected')