# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 17:22:48 2022

@author: 99sma
"""

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

def main():
	x = []
	y = []
	n = int(input("How many point do you want?"))
	#px , py = [] , []
	for i in range(n):
		x.append(int(input(str(i + 1) +"th point x : ")))
		y.append(int(input(str(i + 1) +"th point y : ")))
	
	l=len(x)
	t = []
	m = int(input("How many m do you want?"))
	for i in range(m+1):
		t.append(float(input(str(i + 1) +"th U : ")))

	p = int(input("How many P do you want?"))
	
	tck=[t,[x,y],p]
	
	u3=np.linspace(0,1,(max(l*2,70)),endpoint=True)
	out = interpolate.splev(u3,tck)

	plt.plot(x,y,'k--',label='Control polygon',marker='o',markerfacecolor='red')
	plt.plot(out[0],out[1],'b',linewidth=2.0,label='B-spline curve')
	plt.legend(loc='best')
	plt.axis([min(x)-1, max(x)+1, min(y)-1, max(y)+1])
	plt.title('Cubic B-spline curve evaluation')
	plt.show()


if __name__ == '__main__':
	main()




