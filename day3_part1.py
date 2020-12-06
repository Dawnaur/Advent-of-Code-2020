#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day3_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/03 08:46:35 by Dawnaur           #+#    #+#              #
#    Updated: 2020/12/03 08:46:48 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

count = 0
position = 0
for line in open(sys.argv[1], "r").readlines():
	if (line[position % (len(line) - 1)] == '#'):
		count += 1
	position += 3
print(count)
