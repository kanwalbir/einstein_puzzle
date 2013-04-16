#-----------------------------------------------------------------------------#
"""
Extract the lists for various catagories from the solutions tuple. These lists 
contain house numbers which can be matched with orginal values via list index. 
Finally format and print the results on the screen.

Args: (i)  Puzzle solutions as a tuple of lists (see main.py for more details)

Returns: (i) None (only prints to screen)
"""
def print_puzzle(solutions):

    cig_sols, color_sols, drink_sols, nation_sols, pet_sols = solutions
    print solutions

    cigs = ['Blend', 'Blue Masters', 'Dunhills', 'Pall Mall', 'Prince']
    colors = ['Blue', 'Green', 'Red', 'White', 'Yellow']
    drinks = ['Bier', 'Coffee', 'Milk', 'Tea', 'Water']
    nations = ['Dane', 'Englishman', 'German', 'Norwegian', 'Swede']
    pets = ['Birds', 'Cats', 'Dogs', 'Horses', 'Fish']

    einstein = {}
    for i in range(1,6):
        einstein[i] = {'Nations':'', 'Colors':'', 'Cigarettes':'', 'Drinks':'', 'Pets':''}

    for i in range(5):
        einstein[nation_sols[i]]['Nations'] = nations[i]
        einstein[color_sols[i]]['Colors'] = colors[i]
        einstein[cig_sols[i]]['Cigarettes'] = cigs[i]
        einstein[drink_sols[i]]['Drinks'] = drinks[i]
        einstein[pet_sols[i]]['Pets'] = pets[i]

    print '\n\n', "-" * 71
    print "", "%-9s %-13s %-10s %-16s %-10s %-10s" \
              %('House', 'Nations', 'Colors', 'Cigarettes', 'Drinks', 'Pets')
    print "-" * 71
    for e in einstein:
        print "  ", "%-7s %-13s %-10s %-16s %-10s %-10s" \
                    %(e, einstein[e]['Nations'], einstein[e]['Colors'], \
                      einstein[e]['Cigarettes'], einstein[e]['Drinks'], einstein[e]['Pets'])
    print "-" * 71, '\n\n'

#-----------------------------------------------------------------------------#
