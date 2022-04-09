import time
import numpy as np

"""
Replace following with your own algorithm logic

Two random coordinate generator has been provided for testing purposes.
Manual mode where you can use your mouse as also been added for testing purposes.
"""
def GetLocation(env, current_frame, previous_frame, coordinate, previous_coordinate):
    diff = current_frame - previous_frame
    black = np.column_stack(np.where(diff > 0))
    if len(black) == 0:
        black = np.column_stack(np.where(diff < 0))
    coordinate = coordinate if len(black) == 0 else tuple(black[int(len(black)/2)])
    if len(coordinate) == 3:
        coordinate = coordinate[:2]
    
    return [{'coordinate' : coordinate if coordinate != previous_coordinate else previous_coordinate, 'move_type' : "absolute"}]

