#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day9_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/10 18:37:19 by Dawnaur           #+#    #+#              #
#    Updated: 2020/12/10 18:37:23 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

data = []
previous = [0] * 25
for line in open(sys.argv[1], "r").readlines():
	data.append(int(line))
for i in range(25):
	previous[i] = data[i]

for i in range (25, len(data)):
	ok = 0
	for nb1 in range(24):
		if (ok == 0):
			for nb2 in range(nb1 + 1, 25):
				if (previous[nb1] + previous[nb2] == data[i]):
					ok = 1
	if (ok == 0):
		print(data[i])
	previous[i % 25] = data[i]
