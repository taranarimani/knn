import math


def euclidean_distance(vec1, vec2):
    for i in range(len(vec1)-1):
        distance = distance+math.pow((vec1[i]-vec2[2]), 2)
    return math.sqrt(distance)
