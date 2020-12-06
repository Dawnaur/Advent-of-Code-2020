#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day1_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/01 23:13:06 by Dawnaur           #+#    #+#              #
#    Updated: 2020/12/01 23:13:20 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

max_size = 2020
table = [0] * (max_size + 1)

fd = open(sys.argv[1], "r")
content = fd.readlines()
for number in content:
	table[int(number)] = 1

for i in range(0, int(max_size / 3)):
	for j in range(i, int(i + (max_size / 2))):
		if ((max_size - i - j) >= 0 and (i + j) > int(max_size / 2) and table[i] and table[j] and table[max_size - i - j]):
			print(str(i * j * (max_size - i - j)))
