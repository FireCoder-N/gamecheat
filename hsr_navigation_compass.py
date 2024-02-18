#######################################
# Game: Honkai: Star Rail (miHoYo)
# Location: The Xianzhou Luofu
# Objective: Navigation Compass puzzle
# Description:
#       Various compasses are placed on the area. Each compass is an individual puzzle.
#       The goal is to align the compass needle to the correct direction (left).
#       Each compass has 3 dials and 3 possible rotation-sets. 
#       Each rotation-set rotates either one or two dials. One dial can be rotated by more than one rotation-set.
#       The Bright Astral Marks on the compass dial indicate the degrees it can rotate. Each bright Astral Mark corresponds to a 60° rotation per turn.
#       Two types of rotations exist: clockwise and counterclockwise, indicated by the bright arrow on each dial.
#
# About:
#       This is a simple python script to solve the compass puzzle.
#       Since the puzzle if a dial can be rotated alone is really simple, the script is designed to solve the puzzle only for those cases, where each rotation-set will rotate 2 dials at once.
#       Thus, outer dial is rotated by the first and third rotation-set, the middle dial by the first and second rotation-set and the inner dial by the second and third rotation-set.
#       The script will test all possible combinations of rotations and print the correct combination(s), with k,l,m being the number of turns for the first, second and third rotation-set, respectively.
#       From the above, the script essentially solves a very specific 3x3 system of linear equationsb by brute force.
#       We assume the typical trigonometric circle, where 0° is the rightmost point and the angle increases counterclockwise.
#       All angles are given in degrees and normalized between 0 and 360.
#
# Ideas for further improvement:
#######################################


def normalize(x):
    # Normalize the angle to be between 0 and 360
    if x > 360:
        return x-360
    elif x < 0:
        return x+360
    else:
        return x

def test(x):
    # Test if the angle is an odd multiple of 180
    if x % 180 == 0 and (x/180)%2 == 1:
        return True
    else:
        return False
    
# Initial angles for the compass dials (direction of the needle)
# [edit as needed]
a_init = 180
b_init = 60
c_init = -60

# Rotation of the dials
# [edit as needed]
a_rot = 120
b_rot = -60
c_rot = -240

# Test all possible combinations of rotations (10 is a random but adequate number)
for k in range(10):
    for l in range(10):
        for m in range(10):
            a = normalize(a_init + a_rot*(k+m))
            b = normalize(b_init + b_rot*(k+l))
            c = normalize(c_init + c_rot*(l+m))
            if test(a) and test(b) and test(c):
                print(k,l,m) #k,l,m = # of turns for 1st, 2nd and 3rd rotation-set, respectively
            
    
