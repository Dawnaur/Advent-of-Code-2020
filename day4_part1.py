#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day4_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/04 08:48:25 by Dawnaur           #+#    #+#              #
#    Updated: 2020/12/04 08:48:39 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

count = 0
fields = 0
values = {
	'byr': 1,
	'iyr': 2,
	'eyr': 4,
	'hgt': 8,
	'hcl': 16,
	'ecl': 32,
	'pid': 64,
	'cid': 128
}

for line in open(sys.argv[1], "r").readlines():
	if len(line) <= 1:
		if (fields == 255 or fields == 127):
			count += 1
		fields = 0
	for field in line.split():
		fields |= values[field.split(":")[0]]
print(count)
