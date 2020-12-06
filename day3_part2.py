#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day3_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/06 00:30:08 by Dawnaur           #+#    #+#              #
#    Updated: 2020/12/06 00:30:30 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def get_tree_nb(x_increment, y_increment):
	count = 0
	position = 0
	line_nb = 0
	for line in open(sys.argv[1], "r").readlines():
		if ((line_nb % y_increment) == 0):
			if (line[position % (len(line) - 1)] == '#'):
				count += 1
			position += x_increment
		line_nb += 1
	return (count)

print(get_tree_nb(1, 1) * get_tree_nb(3, 1) * get_tree_nb(5, 1) * get_tree_nb(7, 1) * get_tree_nb(1, 2))
