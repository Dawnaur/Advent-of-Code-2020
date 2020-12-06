#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day2_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/02 19:53:32 by Dawnaur           #+#    #+#              #
#    Updated: 2020/12/02 19:53:46 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

count = 0
for line in open(sys.argv[1], "r").readlines():
	table = line[:-1].split(" ")
	if (table[2].count(table[1][:-1]) in range(int(table[0].split("-")[0]), int(table[0].split("-")[1]) + 1)):
		count += 1
print(count)
