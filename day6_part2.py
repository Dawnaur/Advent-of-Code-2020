#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day6_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/06 06:11:01 by Dawnaur           #+#    #+#              #
#    Updated: 2020/12/06 06:11:07 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

count = 0
fields = 0
table = [1] * (26)

for line in open(sys.argv[1], "r").readlines():
	if len(line) <= 1:
		for i in range(26):
			if table[i] == 1:
				count += 1
		table = [1] * (26)
	else:
		second_table = [0] * (26)
		for letter in line[:-1]:
			second_table[ord(letter) - ord('a')] = 1
		for i in range(26):
			table[i] = table[i] and second_table[i]
print(count)
