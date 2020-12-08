#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day7_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/08 01:33:08 by Dawnaur           #+#    #+#              #
#    Updated: 2020/12/08 01:33:25 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def get_number(bags_list, bag):
	count = 0
	if not bag in bags_list:
		return (0) 
	for b in bags_list[bag]:
		count += (int(b[0]) * (1 + get_number(bags_list, b[1])))
	return (count)

bags = {}

for line in open(sys.argv[1], "r").readlines():
	content = line.split()
	bag = content[0] + content[1]
	content = content[4:]
	bag_content = []
	while (len(content) > 3):
		bag_content.append([content[0], content[1] + content[2]])
		content = content[4:]
	if bag_content:
		bags[bag] = bag_content

print(get_number(bags, "shinygold"))
