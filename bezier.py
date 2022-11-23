# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 17:22:18 2022

@author: 99sma
"""

import math
import matplotlib.pyplot as plt


u = 0.001

def binomial(i, n):
    return math.factorial(n) / float(
        math.factorial(i) * math.factorial(n - i))


def bezier(px , py , u , x , y):
	n = len(px)
	for i in range(n):
		bio = binomial(i , n - 1)
		t = 0
		while t < 1:
			resX = math.pow(t , i) * math.pow( (1 - t) , n - i - 1) * px[i]
			resY = math.pow(t , i) * math.pow( (1 - t) , n - i - 1) * py[i]
			x.append(bio * resX)
			y.append(bio * resY)
			t = t + u
	for i in range(n - 1):
		for j in range(1000):
			x[j] = x[j] + x[(1000*(i+1)) + j]
			y[j] = y[j] + y[(1000*(i+1)) + j]

def main():
	x = []
	y = []
	n = int(input("How many point do you want?"))
	px , py = [] , []
	for i in range(n):
		px.append(int(input(str(i + 1) +"th point x : ")))
		py.append(int(input(str(i + 1) +"th point y : ")))

	bezier(px , py , u , x , y)
	x = x[:1000]
	y = y[:1000]

	plt.plot(x , y)
	plt.show()


if __name__ == '__main__':
	main()