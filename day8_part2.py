#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day8_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/09 02:45:22 by Dawnaur           #+#    #+#              #
#    Updated: 2020/12/09 02:45:26 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

accumulator = 0
pc = 0
error = 0

def acc(op):
	global pc
	global accumulator
	if (op[0] == "+"):
		accumulator += int(op[1:])
	if (op[0] == "-"):
		accumulator -= int(op[1:])
	pc += 1

def jmp(op):
	global pc
	if (op[0] == "+"):
		pc += int(op[1:])
	if (op[0] == "-"):
		pc -= int(op[1:])

def nop(op):
	global pc
	pc += 1

optable = {
	'acc': acc,
	'jmp': jmp,
    'nop': nop
}

table_invert = {
	'jmp': 'nop',
    'nop': 'jmp'
}

def execute(programm):
	global pc
	global error
	global accumulator
	pc = 0
	error = 0
	accumulator = 0
	while 1:
		if (pc >= len(programm)):
			return (accumulator)
		if (programm[pc][2] == 0):
			error = 1
			return (pc)
		programm[pc][2] = 0
		optable[programm[pc][0]](programm[pc][1])
	return (exit)

programm = []
for line in open(sys.argv[1], "r").readlines():
	programm.append([line.split()[0], line.split()[1], 1])
result = execute(programm)

for i in range(len(programm)):
	if ((error != 0) and ((programm[i][0] == "jmp") or (programm[i][0] == "nop"))):
		programm[i][0] = table_invert[programm[i][0]]
		for line in programm:
			line[2] = 1
		result = execute(programm)
		programm[i][0] = table_invert[programm[i][0]]

print(result)




