#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day2_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/02 20:12:19 by Dawnaur           #+#    #+#              #
#    Updated: 2020/12/02 20:12:33 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

count = 0
for line in open(sys.argv[1], "r").readlines():
	table = line[:-1].split(" ")
	if ((table[2][int(table[0].split("-")[0]) - 1] == table[1][0]) != (table[2][int(table[0].split("-")[1]) - 1] == table[1][0])):
		count += 1
print(count)
