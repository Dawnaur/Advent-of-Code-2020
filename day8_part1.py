#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day8_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/09 02:21:10 by Dawnaur           #+#    #+#              #
#    Updated: 2020/12/09 02:21:12 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

accumulator = 0
pc = 0

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

def execute(programm):
	global pc
	while 1:
		if ((pc >= len(programm) or (programm[pc][2] == 0))):
			return (accumulator)
		programm[pc][2] = 0
		optable[programm[pc][0]](programm[pc][1])
	return (exit)

programm = []
for line in open(sys.argv[1], "r").readlines():
	programm.append([line.split()[0], line.split()[1], 1])
print(execute(programm))




