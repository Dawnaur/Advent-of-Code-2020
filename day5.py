#!/usr/bin/python3

# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    day5_part1.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: Dawnaur <dawnaur@outlook.fr>               +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/12/05 04:00:20 by Dawnaur           #+#    #+#              #
#    Updated: 2020/12/05 04:00:35 by Dawnaur          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

nb_max = 0
seats = []
position = 0
for line in open(sys.argv[1], "r").readlines():
	seat_nb = 0
	for direction in line[:7]:
		seat_nb = seat_nb * 2 + (direction == "B")
	for direction in line[7:10]:
		seat_nb = seat_nb * 2 + (direction == "R")
	seats.append(seat_nb)
	if (seat_nb > nb_max):
		nb_max = seat_nb

print("max=" + str(nb_max))
sorted_seat_list = sorted(seats)
first = sorted_seat_list[0]
for seat_nb in sorted_seat_list:
	if (seat_nb != first):
		print("mine=" + str(seat_nb - 1))
		first = seat_nb
	first += 1
	