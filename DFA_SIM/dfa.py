"""
Dfa Sim
--------

This code will take a dict. of dict's as its structure
this structure will be fed into a sim_DFA obj. which will 
then simulate the given string on the structure.

You can define any \Sigma you want, but the set of all 
bit strings are the easiest to get working since its just 
a binary alphabet.

The output will show the path for which the string simulates through
the given states, then the final output will be True or False statement 
about whether the string has been accepted when the DFA halted.
"""


"""
This class will take in the following params

 - transition function and state's (see dfa)
 - q0, i.e. the start state
 - accp, the set of accepting states

When obj of this class is created it will create an obj that will
allow you to pass it the above 3 params; which in return will allow
for the simulation of the DFA to take place.

To run just call your obj.simulate(<Some String>)

Above will return a list of states visited, and the binary eval
of the strings acceptance.
"""
class Sim_DFA:
    def __init__(self, delta, q0, accp):
        self.delta = delta
        self.q0 = q0
        self.accp = accp
    
    def simulate(self, s):
        state = self.q0
        visited = [state]
        for curr in s:
            state = self.delta[state][curr]
            visited.append(state)
        return state in self.accp, visited

"""
{'char':q_n}
Following is set up for 
{all bitstrings with 2n # of 1's}
"""
dfa = {
    0:{'0':0, '1':1},
    1:{'0':1, '1':0}
}


my_dfa = Sim_DFA(dfa, 0, {0})

strings = []
for i in range(1):
    tmp_str = input('Enter String: ')
    strings.append(tmp_str)
print('----------------')    

for string in strings:
    print('Running {}'.format(string))
    result, visited_states = my_dfa.simulate(string)

    for i, state in enumerate(visited_states):
        if (i == len(visited_states) - 1):
            print('s_{}'.format(state))
        else:
            print('s_{}'.format(state), '->', end=' ')
    print('Accepted:', result, '\n')
