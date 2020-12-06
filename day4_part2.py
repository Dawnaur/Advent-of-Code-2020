#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day4_part2.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/04 09:10:09 by Dawnaur           #+#    #+#              #
#    Updated: 2020/12/04 09:10:23 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
import re

def check_byr(value):
	if (int(value) >= 1920 and int(value) <= 2002):
		return 1
	else:
		return 0

def check_iyr(value):
	if (int(value) >= 2010 and int(value) <= 2020):
		return 2
	else:
		return 0

def check_eyr(value):
	if (int(value) >= 2020 and int(value) <= 2030):
		return 4
	else:
		return 0

def check_hgt(value):
	if ((value[-2:] == "cm" and (int(value[:-2]) >= 150 and int(value[:-2]) <= 193))
		or (value[-2:] == "in" and (int(value[:-2]) >= 59 and int(value[:-2]) <= 76))):
		return 8
	else:
		return 0

def check_hcl(value):
	if (re.match(r"^\#[a-f0-9]{6}$", value)):
		return 16
	else:
		return 0

def check_ecl(value):
	colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
	if (value in colors):
		return 32
	else:
		return 0

def check_pid(value):
	if (re.match(r"^[0-9]{9}$", value)):
		return 64
	else:
		return 0

def check_cid(value):
	return 128

values = {
	'byr': check_byr,
	'iyr': check_iyr,
	'eyr': check_eyr,
	'hgt': check_hgt,
	'hcl': check_hcl,
	'ecl': check_ecl,
	'pid': check_pid,
	'cid': check_cid
}

count = 0
fields = 0
line_nb = 0

for line in open(sys.argv[1], "r").readlines():
	line_nb += 1
	if len(line) <= 1:
		if (fields == 255 or fields == 127):
			count += 1
		fields = 0
	for field in line.split():
		fields |= values[field.split(":")[0]](field.split(":")[1])
print(count)
