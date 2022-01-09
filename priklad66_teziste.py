from statistics import mean
import matplotlib.pyplot as plt
import json
with open("input_cr.geojson", encoding="utf-8") as a:
    okresy = json.load(a)

vertices = okresy['features'][0]['geometry']['coordinates'][0]

x, y = zip(*vertices)
A = 0
centroid_x = 0
centroid_y = 0
for i in range(1, len(vertices)):
    A += (x[i-1]*y[i])-(x[i]*y[i-1])
    centroid_x += (x[i-1]+x[i])*(x[i-1]*y[i]-x[i]*y[i-1])
    centroid_y += (y[i-1]+y[i])*(y[i]*x[i-1]-y[i-1]*x[i])
centroid_x = centroid_x/(3*A)
centroid_y = centroid_y/(3*A)
print(A)
print(centroid_x)
print(centroid_y)

plt.figure()
plt.plot(x, y)
plt.scatter(centroid_x, centroid_y)
plt.show()
