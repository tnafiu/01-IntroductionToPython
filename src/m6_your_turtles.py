"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Toluwa Nafiu.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################
import rosegraphics as rg
###############################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################
alex = rg.SimpleTurtle('turtle')
jimbo = rg.SimpleTurtle('turtle')
alex.pen = rg.Pen('green', 10)
jimbo.pen = rg.Pen('blue', 10)

size = 156

for k in range(12):
    alex.draw_square(size)

    alex.pen_up()
    alex.right(45)
    alex.forward(15)
    alex.left(45)

    alex.pen_down()

    jimbo.draw_square(size)

    jimbo.pen_up()
    jimbo.forward(25)
    jimbo.right(45)
    jimbo.forward(25)
    jimbo.left(45)

    jimbo.pen_down()
    size = size - 12
