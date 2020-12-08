#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day7_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/07 07:44:48 by Dawnaur           #+#    #+#              #
#    Updated: 2020/12/08 01:32:42 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def get_number(bags_list, bag):
	count = 0
	tocheck = []
	for b in bags_list:
		found = 0
		for link in bags_list[b]:
			if ((found == 0) and (link[1] == bag)):
				found = 1
		if (found == 1):
			tocheck.append(b)
			count += 1
	for b in tocheck:
		del bags_list[b]
	for b in tocheck:
		count += get_number(bags_list, b)
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
