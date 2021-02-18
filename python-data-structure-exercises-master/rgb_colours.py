# This program knows about the RGB code corresponding to common colours.
#
# Usage:
#
# $ python rgb_colours.py [colour]
#
# For instance:
#
# $ python rgb_colours.py red
# The RGB code for red is F00
#
# or:
#
# $ python rgb_colours.py "burnt sienna"
# I don't know the RGB code for burnt sienna


import argparse
parser = argparse.ArgumentParser() 
parser.add_argument("color", help="pass in station", nargs="?")
args = parser.parse_args()



colours = [
     ['red', 'F00'],
['yellow', 'FF0'],
 ['green', '0F0'],
 ['cyan', '0FF'],
  ['blue', '00F'],
  ['magenta', 'F0F'],
]


# TODO:
# * Implement the program as described in the comments at the top of the file.
for color, code in colours:
    if color == args.color.lower():
        ans = "The RGB code for {} is {}".format(color, code)
        print(ans)
    
    if  code ==args.color.upper():
        ans = "The color name for {} is {}".format( code, color)
        print(ans)





#

# TODO (extra):
# * Change the program so that users can also enter an RGB colour code, and be
#   told the name of the corresponding colour.
# * Change the program so that it ignores the case of the user's input.
