"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Nelson Rainey.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
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
#
########################################################################

import rosegraphics as rg


nelson= rg.SimpleTurtle()
nelson.pen=rg.Pen('blue',10)
nelson.speed= 3

size = 150

for k in range(2):
    nelson.draw_square(150)
    nelson.pen_up()
    nelson.right(180)
    nelson.forward(200)
    nelson.right(90)




    nelson.pen_down()

for j in range(1):
    nelson.pen_up()

    nelson.left(90)
    nelson.forward(100)

    nelson.pen_down()

    nelson.draw_circle(130)

nick=rg.SimpleTurtle()
nick.pen=rg.Pen('brown',5)
nick.speed = 2

for k in range(1):
    nick.pen_up()
    nick.forward(75)
    nick.left(90)
    nick.forward(75)
    nick.pen_down()
    nick.draw_circle(10)
    nick.pen_up()
    nick.left(90)
    nick.forward(350)
    nick.pen_down()
    nick.draw_circle(10)


