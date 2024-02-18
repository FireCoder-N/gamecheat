#######################################
# Game: Honkai: Star Rail (miHoYo)
# Location: Everwinter City Museum
# Objective: Museum Management
# Description:
#       Players accumulate RevitaScore by upgrading the various exhibition areas of the Museum using Development Fund and completing rounds of Management. 
#       RevitaScore can also be obtained by unlocking new Exhibits and Guest Assistants.
#       During Management, the total amount of RevitaScore obtained at the end of each round will depend on the acquired Rank and upgrade level of each Exhibition Area.
#       Upon accumulating a certain amount of RevitaScore, the player will progress into the next management phase.
#       Each new phase will unlock other halls and further upgrade levels for each section of each hall.
#
#       The Rank of an exhibition area will depend on whether or not the needs of that area are met.
#        There are 3 main needs per area:
#          - Tour Duration
#          - Education Value
#          - Visitor Appeal
#
#        The player can fill the various needs by recruiting better Staff and by upgrading the "Tour Guidance", "Education Materials" and "Visitor Promotion" parameters of each exhibition area.
#        There are 4 ranks that can be obtained at the end of Management:
#          C: The area is lacking in every need
#          B: The area is lacking in 2 needs
#          A: The area is lacking in 1 need
#          S: The area has all needs filled
#
#        The lower the rank, the less RevitaScore the player will obtain per round of Management.
#
#
# About:
#       Each area has 3 criteria that need to be met to obtain the maximum rank (S).
#       Each staff member has a value for each of the 3 criteria.
#       The player can only have 3 staff members in each area.
#       Given a room's goals/criteria to be achieved (X_value, Y_value, Z_value), the code will find a combination of 3 staff members (among the available options) to achive an S rank.
#
# Ideas for further improvement:
#       Find all possible satisfying combinations.
#       Simultaneously achieve S Rank in all of the museums rooms, removing the chosen staff from the available options after each room is solved.
#       Find the best possible combination, in case not all the requirements can be met, so that the player will need to do minimum upgrades the room to achieve S Rank.
#######################################


from itertools import combinations

def find_combination(options, X, Y, Z):
    # Generate all combinations of 3 elements from the options
    possible_combinations = combinations(options, 3)

    # Check each combination
    for combination in possible_combinations:
        # Unpack the combination
        N1, N2, N3 = combination

        # Check if the combination satisfies the equations
        if (N1[0] + N2[0] + N3[0] >= X) and (N1[1] + N2[1] + N3[1] >= Y) and (N1[2] + N2[2] + N3[2] >= Z):
            return combination  # Return the satisfying combination

    return None  # Return None if no satisfying combination is found

# Available staff members' values for each criteria
available_options = [
    #[93, 93, 0],
    [56, 72, 40],
    [63, 0, 63],
    [52, 20, 36],
    [30, 30, 30],
    [94, 86, 0],
    [64, 20, 78],
    [10, 58, 73],
    [42, 22, 65],
    [44, 54, 10],
    [36, 40, 20],
    [40, 8, 30],
    #[18, 80, 82],
    [5, 80, 83],
    [78, 9, 39],
    [54, 54, 0],
    [52, 14, 30],
    [26, 26, 26],
    [48, 23, 85],
    [10, 66, 50],
    [8, 58, 42],
    [50, 29, 17],
    [20, 44, 14],
    [66, 60, 15],
    [54, 16, 71],
    #[12, 62, 88]
    # Add more options as needed
]

# goal scores for the room
X_value = 106 # Tour Duration
Y_value = 105 # Education Value
Z_value = 135 # Visitor Appeal

result = find_combination(available_options, X_value, Y_value, Z_value)

if result:
    print(f"Satisfying combination found: {result}")
else:
    print("No satisfying combination found.")
