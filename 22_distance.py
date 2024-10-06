def dist(points):
    max = points[0]
    min = points[0]
    for i in range(len(points)):
        if (points[i] > max):
            max = points[i]
        elif(points[i] < min):
            min = points[i]
    return(max - min)
    
