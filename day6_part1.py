#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day6_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/06 05:52:03 by Dawnaur           #+#    #+#              #
#    Updated: 2020/12/06 05:52:17 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

count = 0
fields = 0
table = [0] * (26)

for line in open(sys.argv[1], "r").readlines():
	if len(line) <= 1:
		for i in range(26):
			if table[i] == 1:
				count += 1
		table = [0] * (26)
	else:
		for letter in line[:-1]:
			table[ord(letter) - ord('a')] = 1
print(count)
