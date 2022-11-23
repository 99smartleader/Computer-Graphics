# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 17:22:18 2022
@author: 99smartleader/smartwolf99
"""
import math
import matplotlib.pyplot as plt

x = []
y = []
u = 0.001

def hermite(px , py , qx , qy , prx , pry , qrx , qry , u):
	tt = u
	while(tt < 1):
		resx = (1-3*math.pow(tt,2)+2*math.pow(tt,3))*px+(3*math.pow(tt,2)-2*math.pow(tt,3))*qx+(tt-2*math.pow(tt,2)+math.pow(tt,3))*prx+(-math.pow(tt,2)+math.pow(tt,3))*qrx;
		resy = (1-3*math.pow(tt,2)+2*math.pow(tt,3))*py+(3*math.pow(tt,2)-2*math.pow(tt,3))*qy+(tt-2*math.pow(tt,2)+math.pow(tt,3))*pry+(-math.pow(tt,2)+math.pow(tt,3))*qry;
		x.append(resx)
		y.append(resy)
		tt = tt+u

def main():
	n = int(input("How many point do you want?"))
	px , py , qx , qy , prx , pry , qrx , qry = [] , [] , [] , [] , [] , [] , [] , []
	for i in range(n):
		px.append(int(input(str(i + 1) +"th point x : ")))
		py.append(int(input(str(i + 1) +"th point y : ")))
		prx.append(int(input(str(i + 1) +"th point rx : ")))
		pry.append(int(input(str(i + 1) +"th point ry : ")))
		if(i > 0):
			hermite(px[i - 1] , py[i - 1] , px[i] , py[i] , prx[i - 1] , pry[i - 1] , prx[i] , pry[i] , u)

	plt.plot(x , y)
	plt.show()


if __name__ == '__main__':
	main()
