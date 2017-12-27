# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

def drawAPicture(xs, picname, pictitle):
	xs.sort()
	x = []
	y = []
	fst = xs[0]
	lst = xs[-1]
	x = map(lambda x: fst + (lst - fst) * 1. / 10 * x, range(0, 10))
	y = [0] * 10
	for xx in xs:
		for yy in xrange(9, -1, -1):
			if xx >= x[yy]:
				y[yy] = y[yy] + 1
				break
	plt.bar(x, y, (lst - fst) / 20, color = "rgb")
	plt.xlabel(pictitle)
	plt.ylabel("Count")
	plt.title(pictitle)
	plt.savefig(picname)
	plt.clf()

def drawPicture(results, yPng, dPng, cPng):
	yields = []
	durations = []
	convexities = []
	for result in results:
		yields.append(result["Yield"])
		durations.append(result["Duration"])
		convexities.append(result["Convexity"])
	drawAPicture(yields, yPng, "Yields")
	drawAPicture(durations, dPng, "Durations")
	drawAPicture(convexities, cPng, "Convexities")

