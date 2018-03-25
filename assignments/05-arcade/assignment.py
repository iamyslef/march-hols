import math
# Part 1 - figuring out whether the boss is dead
def boss_dead(t, a, x, b):
    """
    Args:
        t: int
            The time that we want to check whether the boss is dead.
            For instance, boss_dead(10, a, x, b) returns whether the
            boss is dead 10 seconds after the game starts.
        a: int
            Interval at which Aaron deals a damage
        x: int
            Interval at which Xuanchun deals a damage
        b: int
            Amount of damage a boss can take before it is dead
    Returns:
        A boolean, where True means the boss is dead and False means the boss is not
    """

    # Your code here
    aarondmg = math.floor(t / a)
    xcdmg = math.floor(t / x)
    if(aarondmg + xcdmg >= b):
        return True
    elif(aarondmg + xcdmg < b):
         return False
boss_dead()

# Part 2 - figuring out when the game ends
def game_length(a, x, b):
    """
    Args:
        a: int
            Interval at which Aaron deals a damage
        x: int
            Interval at which Xuanchun deals a damage
        b: int
            Amount of damage a boss can take before it is dead
    Returns:
        An int, the amount of time it takes for the game to be over.
    """

    # Your code here
    t = 0
    aarondmg = math.floor(t / a)
    xcdmg = math.floor(t / x)
    while t < 10000000000000000000:
        if(aarondmg + xcdmg >= b):
            return t
        elif(aarondmg + xcdmg < b):
            t = t + 1
game_length()

# Part 3 - answer
"""
This part does not require any code to be written. Suppose that we have a=1000, x=1000, b=10^9, how long does it take for the game to end? Will your code for Part 2 give a satisfactory running time for this case?
500000 seconds
Another important observation to make: if the boss is dead at t=t0, will it be alive at t = t0 + 1? How about t = t0 + 109?
wot
"""

# Part 4 - optimised code using binary search
def game_length_opt(a, x, b):
    """
    Args:
        a: int
            Interval at which Aaron deals a damage
        x: int
            Interval at which Xuanchun deals a damage
        b: int
            Amount of damage a boss can take before it is dead
    Returns:
        An int, the amount of time it takes for the game to be over.
    """

    l = 0
    r = 10**18

    while(r - l > 1):
        guess = (r + l) // 2 # // stands for floored division
        if """some condition""":
            # do something

            # do some other thing

    return r

if __name__ == '__main__':
    print(boss_dead(0, 1, 1, 10))
    print(boss_dead(4, 1, 1, 10))
    print(boss_dead(4, 1, 6, 7))
    # Add your own tests after this line
