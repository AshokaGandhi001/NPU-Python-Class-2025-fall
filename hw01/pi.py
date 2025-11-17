import random
import math

"""

"""
line_distance = 1.0
needle_length = line_distance / 2

def buffon_needle_simulation(times): 
    crossed_time = 0
    for _ in range(times):
        needle_center = random.uniform(0, line_distance)
        theta = random.uniform(0, math.pi)

        vertical_length = needle_length * math.sin(theta)

        crossed = needle_center <= vertical_length / 2 or (line_distance - needle_center) <= vertical_length / 2

        if crossed:
            crossed_time += 1

    assert crossed_time > 0
    try :
        estimated_pi = times / crossed_time
    except AssertionError as e:
        print(f"{e}, 不能除以0")

    return estimated_pi

