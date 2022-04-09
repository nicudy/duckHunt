import time
import numpy as np

"""
This function determines where the target should move to next based on bird placement
"""
def GetLocation(env, current_frame, previous_frame):
	# get the difference between the current frame pixels and the previous frame
    diff = current_frame - previous_frame
    # detects if (a) bird(s) has moved right and/or down
    birds = np.column_stack(np.where(diff > 0))
    # if they haven't moved right and/or down
    if len(birds) == 0:
    	# detects if the birds have moved left or up
        birds = np.column_stack(np.where(diff < 0))
    # if the birds have not moved, then return a random coorodinate. 
    #Otherwise, choose the bird in the middle as well as the middle pixel of the bird
    coordinate = tuple(env.action_space_abs.sample()) if len(birds) == 0 else tuple(birds[int(len(birds)/2)])[:2]
    return [{'coordinate' : coordinate, 'move_type' : "absolute"}]

