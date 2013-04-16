#-----------------------------------------------------------------------------#
"""
1.  The Englishman lives in the red house.
2.  The Swede keeps dogs.
3.  The Dane drinks tea.
4.  The green house is just to the left of the white one.
5.  The owner of the green house drinks coffee.
6.  The Pall Mall smoker keeps birds.
7.  The owner of the yellow house smokes Dunhills.
8.  The man in the center house drinks milk.
9.  The Norwegian lives in the first house.
10. The Blend smoker has a neighbor who keeps cats.
11. The man who smokes Blue Masters drinks bier.
12. The man who keeps horses lives next to the Dunhill smoker.
13. The German smokes Prince.
14. The Norwegian lives next to the blue house.
15. The Blend smoker has a neighbor who drinks water.
"""

#-----------------------------------------------------------------------------#
#                            PACKAGE AND MODULE IMPORTS                       #
#-----------------------------------------------------------------------------#

"""
Itertools module import
"""
import itertools

"""
Other Python file imports.
"""
from neighbors import is_next, is_left
from print_einstein import print_puzzle

#-----------------------------------------------------------------------------#
"""
Based on the above statements all the information is catagorized as following:
- Various Nationalities
- House Colors
- Favorite Cigarettes
- Favorite Drinks
- Pets
- House Numbers (assigned from left to right in increasing order)

All possible house number permutations are calculated and then iterated with 
the above catagories. The constraints (if statements) have been ordered under 
appropirate for loops to avoid any processing of additional for loops if the 
constraint does not hold True (False).

Solution is generated in form of a list of tuples and sent to print_puzzle 
for printing.

Args: (i) None (all statements are encoded in this module)

Returns: (i) None (solutions are sent to print_puzzle for printing)
"""
def solve_einstein_puzzle():

    houses = [1,2,3,4,5]   # All the different house numbers
    all_combos = list(itertools.permutations(houses)) # All possible permutations of house numbers
    first = 1
    center = 3

    solutions = next(([blend, blue_masters, dunhills, pall_mall, prince],
                      [blue, green, red, white, yellow], 
                      [bier, coffee, milk, tea, water], 
                      [dane, englishman, german, norwegian, swede], 
                      [birds, cats, dogs, horses, fish]
                     )
                
                # All the different house colors
                for (blue, green, red, white, yellow) in all_combos
                if is_left(green, white)              # Line 4
                
                # All the different nationalities
                for (dane, englishman, german, norwegian, swede) in all_combos
                if englishman == red                  # Line 1
                if norwegian == first                 # Line 9
                if is_next(norwegian, blue)           # Line 14
                
                # All the different drinks
                for (bier, coffee, milk, tea, water) in all_combos
                if dane == tea                        # Line 3
                if green == coffee                    # Line 5
                if center == milk                     # Line 8
                
                # All the different cigarettes
                for (blend, blue_masters, dunhills, pall_mall, prince) in all_combos    
                if yellow == dunhills                 # Line 7
                if blue_masters == bier               # Line 11
                if german == prince                   # Line 13
                if is_next(blend, water)              # Line 15

                # All the different pets
                for (birds, cats, dogs, horses, fish) in all_combos                     
                if swede == dogs                      # Line 2
                if pall_mall == birds                 # Line 6
                if is_next(blend, cats)               # Line 10
                if is_next(horses, dunhills)          # Line 12
            )
    
    print_puzzle(solutions)

#-----------------------------------------------------------------------------#
"""
Test values for above function.
"""
solve_einstein_puzzle()

