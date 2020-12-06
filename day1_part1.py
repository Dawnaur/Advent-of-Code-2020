#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day1_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/01 22:21:10 by dawnaur           #+#    #+#              #
#    Updated: 2020/12/01 22:21:10 by dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

max_size = 2020
table = [0] * (max_size + 1)

fd = open(sys.argv[1], "r")
content = fd.readlines()
for number in content:
	table[int(number)] = 1

for i in range(0, int(max_size / 2)):
	if (table[i] and table[max_size - i]):
		print(str(i * (max_size - i)))
