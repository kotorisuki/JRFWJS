# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

XLENS = 100

def drawAPicture(xs, picname, pictitle):
	xs.sort()
	x = []
	y = []
	fst = xs[0]
	lst = xs[-1]
	x = map(lambda x: fst + (lst - fst) * 1. / XLENS * x, range(0, XLENS))
	y = [0] * XLENS
	for xx in xs:
		for yy in xrange(XLENS - 1, -1, -1):
			if xx >= x[yy]:
				y[yy] = y[yy] + 1
				break
	plt.bar(x, y, (lst - fst) / 2. / XLENS, color = "rgb")
	plt.xlabel(pictitle)
	plt.ylabel("Count")
	plt.title(pictitle)
	plt.savefig(picname)
	plt.clf()

def drawPicture(results, yPng, dPng, cPng, dpPng):
	yields = []
	durations = []
	convexities = []
	dirtyprices = []
	for result in results:
		yields.append(result["Yield"])
		durations.append(result["Duration"])
		convexities.append(result["Convexity"])
		dirtyprices.append(result["DirtyPrice"])
	drawAPicture(yields, yPng, "Yields")
	drawAPicture(durations, dPng, "Durations")
	drawAPicture(convexities, cPng, "Convexities")
	drawAPicture(dirtyprices, dpPng, "DirtyPrices")

