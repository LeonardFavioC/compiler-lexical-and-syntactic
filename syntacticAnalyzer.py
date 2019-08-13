# coding: utf-8

import re
import string
import pandas as pd
from lexicalAnalyzer import getTockens

# Verificación de valores de entradas en la tabla de valores
def parse(user_input,start_symbol,parsingTable):

	#flag
	flag = 0

	# appending dollar to end of input

	user_input = user_input + "$"

	stack = []

	stack.append("$")
	stack.append(start_symbol)

	input_len = len(user_input)
	index = 0


	while len(stack) > 0:

		#element at top of stack
		top = stack[len(stack)-1]

		print ("Stack =>",top)

		#current input
		current_input = user_input[index]

		print ("Current input => ",current_input)

		if top == current_input:
			stack.pop()
			index = index + 1
		else:

			#finding value for key in table
			key = top , current_input
			print (key)

			#top of stack terminal => not accepted
			if key not in parsingTable:
				flag = 1
				break

			value = parsingTable[key]
			if value !='@':
				value = value[::-1]
				value = list(value)

				#poping top of stack
				stack.pop()

				#push value chars to stack
				for element in value:
					stack.append(element)
			else:
				stack.pop()

	if flag == 0:
		print ("Sintax accepted!")
	else:
		print ("Sintax not accepted!"	)


# Dibujar la tabla de valores
def ll1(follow, productions):
	table = {}
	for key in productions:
		for value in productions[key]:
			if value!='@':
				for element in first(value, productions):
					table[key, element] = value
			else:
				for element in follow[key]:
					table[key, element] = value

	new_table = {}
	for pair in table:
		new_table[pair[1]] = {}

	for pair in table:
		new_table[pair[1]][pair[0]] = table[pair]


	print ("\nTable in matrix \n")
	print (pd.DataFrame(new_table).fillna('-'))
	print ("\n")

	return table

def follow(s, productions, ans):
	if len(s)!=1 :
		return {}

	for key in productions:
		for value in productions[key]:
			f = value.find(s)
			if f!=-1:
				if f==(len(value)-1):
					if key!=s:
						if key in ans:
							temp = ans[key]
						else:
							ans = follow(key, productions, ans)
							temp = ans[key]
						ans[s] = ans[s].union(temp)
				else:
					first_of_next = first(value[f+1:], productions)
					if '@' in first_of_next:
						if key!=s:
							if key in ans:
								temp = ans[key]
							else:
								ans = follow(key, productions, ans)
								temp = ans[key]
							ans[s] = ans[s].union(temp)
							ans[s] = ans[s].union(first_of_next) - {'@'}
					else:
						ans[s] = ans[s].union(first_of_next)
	return ans
# Metodo recursivo para calcular los primeros
def first(s, productions):
	c = s[0]
	ans = set()
	if c.isupper():
		for st in productions[c]:
			if st == '@' :
				if len(s)!=1 :
					ans = ans.union( first(s[1:], productions) )
				else :
					ans = ans.union('@')
			else :
				f = first(st, productions)
				ans = ans.union(x for x in f)
	else:
		ans = ans.union(c)
	return ans

def readFile(name):
    try:
        x = open(name, 'r')
        return x
    except:
		return('Something went wrong when reading to the file')
		x.close()

if __name__=="__main__":
	productions=dict()
	# grammar = open("grammar", "r")
	grammar = readFile('grammar')
	first_dict = dict()
	follow_dict = dict()
	flag = 1
	start = ""
	for line in grammar:
		l = re.split("( |->|\n|\||)*", line)
		lhs = l[0]
		rhs = set(l[1:-1])-{''}
		if flag :
			flag = 0
			start = lhs
		productions[lhs] = rhs

	print ('\nFirst\n')
	for lhs in productions:
		first_dict[lhs] = first(lhs, productions)
	for f in first_dict:
		print (str(f) + " : " + str(first_dict[f]))
	print ("")

	print ('\nFollow\n')

	for lhs in productions:
		follow_dict[lhs] = set()

	follow_dict[start] = follow_dict[start].union('$')

	for lhs in productions:
		follow_dict = follow(lhs, productions, follow_dict)

	for lhs in productions:
		follow_dict = follow(lhs, productions, follow_dict)

	for f in follow_dict:
		print (str(f) + " : " + str(follow_dict[f]))

	ll1Table = ll1(follow_dict, productions)

	# parse("n+n*(p(n,n))*i",start,ll1Table)

	for line in getTockens():
		parse(line, start, ll1Table)
		print('\n')
