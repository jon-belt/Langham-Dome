import numpy as np
from locate_points import locateDot, locateReticule

#dot_coords is an array of arrays with length varying from 1-3 dots, ret_coords is just an array
#ret_coords is always [x, y], dot_coords is always at least [[x1, y1], [x2, y2], [x3, y3]]
def calcDist(dot_coords, ret_coords):
    print("calcDist Called")
    #check if dot_coords is -1, then return -1
    if dot_coords == -1:
        return -1
    
    shortest_dist = float('inf')

    #find which dot is closest to the reticule
    for dot in dot_coords:
        #calculate the distance from the current dot to ret_coords
        side1 = (dot[0] - ret_coords[0])
        side2 = (dot[1] - ret_coords[1])
        dist = np.hypot(side1, side2)

        #print(dist)    #for debugging

        #update shortest_dist if a closer dot is found
        if dist < shortest_dist:
            #print("New shortest dist: ", shortest_dist)    #for debugging
            shortest_dist = dist

    return shortest_dist

def calcScore(imgPath, difficulty):
    print("calcScore Called")
    x = locateDot(imgPath)
    y = locateReticule(imgPath)

    distance = calcDist(x, y)
    
    if distance < 0:
        return 0
    
    max_score = 100

    #Difficulty affects how accurate the user has to be
    scale_factors = [0.001, 0.004, 0.0075, 0.01]
    scale_factor = scale_factors[difficulty] if 0 <= difficulty < len(scale_factors) else None

    if scale_factor is None:
        print("Difficulty entered as number outside acceptable range")
        return -1

    score = max_score * np.exp(-scale_factor * distance)
    score = max(0, score)
    return score
