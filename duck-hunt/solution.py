import time
import numpy as np

"""
Replace following with your own algorithm logic

Two random coordinate generator has been provided for testing purposes.
Manual mode where you can use your mouse as also been added for testing purposes.
"""
def GetLocation(env, current_frame, previous_frame):
	
    diff = current_frame - previous_frame
    birds = np.column_stack(np.where(diff > 0))

    if len(birds) == 0:
        birds = np.column_stack(np.where(diff < 0))

    coordinate = tuple(env.action_space_abs.sample()) if len(birds) == 0 else tuple(birds[int(len(birds)/2)])[:2]
    
    return [{'coordinate' : coordinate, 'move_type' : "absolute"}]

