#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day9_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/10 18:48:40 by Dawnaur           #+#    #+#              #
#    Updated: 2020/12/10 18:48:40 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def ft_sum(value_list):
	acc = 0
	for value in value_list:
		acc += value
	return (acc)

magic = 1639024365
data = []
for line in open(sys.argv[1], "r").readlines():
	data.append(int(line))
start = 0
for i in range (2, len(data)):
	res = ft_sum(data[start:i])
	while ((res > magic) and (start + 2 < i)):
		start += 1
		res = ft_sum(data[start:i])
	if (res == magic):
		print(sorted(data[start:i])[0] + sorted(data[start:i])[-1])
