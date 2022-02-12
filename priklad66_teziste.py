try:
    import matplotlib.pyplot as plt
    import json
    import sys
except ImportError:
    sys.exit ("An error occured while importing a library. Check if the required libraries are installed correctly.")

def polygon_area (x,y):
    # returns area of a polygon knowing the coordinates of its vertices
    A=0
    for i in range(1, len(x)):
        A += (x[i-1]*y[i])-(x[i]*y[i-1])
    area = A/2
    return area

def centroid (x,y):
    """
    Computes the coordinates of the centroid of a polygon

    Parameters:
        x (tuple): contains x-coords of vertices of the input polygon
        y (tuple): contains y-coords of vertices of the input polygon
    Returns:
        centroid_coords (tuple): contains coordinates of the centroid of the input polygon
    """
    centroid_x = 0
    centroid_y = 0
    area = polygon_area(x,y)
    for i in range(len(x) - 1):
        centroid_x += (x[i]+x[i+1])*(x[i]*y[i+1]-x[i+1]*y[i])
        centroid_y += (y[i]+y[i+1])*(x[i]*y[i+1]-x[i+1]*y[i])
    centroid_x_final = centroid_x/(6*area)
    centroid_y_final = centroid_y/(6*area)
    centroid_coords = centroid_x_final, centroid_y_final
    return centroid_coords

def visualize (x_polygon, y_polygon, centroid):
    # visualizes the input polygon and its centroid
    fig, ax = plt.subplots()
    fig.suptitle("Centroid of a polygon")
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    ax.plot(x_polygon, y_polygon)
    ax.scatter(*centroid)
    plt.show()

# loads data from the input file
try:   
    with open("input_cr.geojson", encoding="utf-8") as input:
        sample_polygon = json.load(input)
        vertices = sample_polygon['features'][0]['geometry']['coordinates'][0]
except IOError:
    sys.exit ("An error occured while opening the file with input data. Check if the file is in same directory as the script.")
except KeyError:
    sys.exit ("An error ocuured while reading the input data. Check if the file contains the required attributes.")
except:
    sys.exit ("Something went wrong.")

# iterator of tuples, one contains x-coords, seocnd one y-coords of the vertices of the input polygon
x, y = zip(*vertices)

centroid_coords=centroid(x,y)
visualize(x,y,centroid_coords)