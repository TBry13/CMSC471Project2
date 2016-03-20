import math
import random

class proj2:

	def optimise_function (x, y):
		r = math.hypot(x,y)
		z = ((math.sin(x*x + 3*y*y))/0.1 + r*r) + (x*x + 5*y*y) * ((math.exp(1 - r*r))/2)
		return z
		
	def hill_climb(self, function_to_optimize, step, xmin, xmax, ymin, ymax):
		x = 0
		y = 0
		min = function_to_optimize(x, y)
		temp = 10000
		while (temp != min):
			min = compare (min, temp)
			
			if (x - step > xmin):
				z = function_to_optimize(x - step, y)
				temp = compare (z, temp)
				
				
			if (x + step < xmax):
				z = function_to_optimize(x + step, y)
				temp = compare (z, temp)
			
			if (y - step > ymin):
				z = function_to_optimize(x, y - step)
				temp = compare (z, temp)
				
			if (y + step < ymax):
				z = function_to_optimize(x, y + step)
				temp = compare (z, temp)
		
		return min
	
	def hill_climb_random_restart(self, function_to_optimize, step, num_restarts, xmin, xmax, ymin, ymax):
		i=0
		min = 10000
		x = 0
		y = 0
		while i < num_restarts:
			temp = hill_climb(function_to_optimize, step, xmin, xmax, ymin, ymax, x, y)
			min = compare (temp, min)
			x = random.uniform(xmin, xmax)
			y = random.uniform(ymin, ymax)
			i = i + 1
			
		return min
		
	def simulated_annealing(self, function_to_optimize, step, min_temp, xmin, xmax, ymin, ymax):
		x = 0
		y = 0
		i = 0
		t = 1
		temp = function_to_optimize(x, y)
		min = min_temp
		while i < 500:
			min = compare (temp, min)
			xtemp = x
			ytemp = y
			if (x - step > xmin):
				xtemp = random.uniform(x - step, x)
				z = function_to_optimize(xtemp, y)
				if (z < temp):
					temp = z
					x = xtemp
				else:
					if (acceptance_probability(temp, z, t)):
						temp = z
						x = xtemp
					
			if (x + step < xmax):
				xtemp = random.uniform(x, x + step)
				z = function_to_optimize(xtemp, y)
				if (z < temp):
					temp = z
					x = xtemp
				else:
					if (acceptance_probability(temp, z, t)):
						temp = z
						x = xtemp
				
			if (y - step > ymin):
				ytemp = random.uniform(y - step, y)
				z = function_to_optimize(x, ytemp)
				if (z < temp):
					temp = z
					y = ytemp
				else:
					if (acceptance_probability(temp, z, t)):
						temp = z
						y = ytemp
						
			if (y + step < ymax):
				ytemp = random.uniform(y, y + step)
				z = function_to_optimize(x, ytemp)
				if (z < temp):
					temp = z
					y = ytemp
				else:
					if (acceptance_probability(temp, z, t)):
						temp = z
						y = ytemp
						
			t = t * .95
			i = i + 1
		
		return min

	def compare (newMin, oldMin):
		if (newMin < oldMin):
			return newMin
		else:
			return oldMin
			
	def acceptance_probability (old, new, t):
		a = math.exp((old - new) / t)
		temp = random.uniform(0, 1)
		if ( a > temp):
			return True
		else:
			return False
			



c = proj2()

min = c.hill_climb(optimise_function(), .5, -2.5, 2.5, -2.5, 2.5)

print(min)
				