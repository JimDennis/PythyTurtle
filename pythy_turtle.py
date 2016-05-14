#!/usr/bin/env python
'''Illustrate the Pythagorean Theorem Using a Simple Diagram

   This program uses turtle graphics to draw a diagram showing how the Pythagorean Theorem
   could be proven by construction of a set of two large squares each enclosing four
   identical triangles, one leaving smaller squares and the other leaving a larger square
   if the triangles are removed.  The constuction could be done by compass and straight-edge
   although that process is not shown.

   https://xkcd.com/866/
   http://rationalwiki.org/wiki/Compass_and_straightedge_constructions
'''

from __future__ import print_function

TODO='''
    * Put all text in canvas
    * OnKey and OnClick interaction
    * Make interaction optional
    * Export to SVG
        http://stackoverflow.com/q/25050156/149076
        https://pypi.python.org/pypi/canvasvg/1.0.0
    * Add background image (of Pythagoras' face?)
    * Add "straight edge" and "compass" sprites
        * Animate them?
    * Post to GitHub
    * Use ratio and scale (custom) triangles to canvas size
    * Shift diagram towards the upper right
'''

__author__ = 'James T. Dennis'
__copyright__ = '(c) 2016 James T. Dennis'
__license__ = 'BSD'
__version__ = '0.0.2'

import turtle


def draw_diagram(height=50, width=100):
    '''Returns Screen
    '''
    w = turtle.Screen()
    w.title('Pythagorean Theorem Diagram')
    t = turtle.Turtle()
    ht = height
    wd = width

    # TODO: check height/width for too big ... scale? adjust winsize?
    if 2*(ht+wd) > w.window_width() or (ht+wd) > w.window_height():
        print("This diagram won't fit in the window")
        print('Drawing it anyway')

    # cardinal directions
    east = 0
    north = 90
    west = 180
    south = 270

    # pen thicknesses:
    thick = 4
    thin = 2
    vthin = 1

    pale_cyan = '#88F4F0'
    lavender  = '#F388D7'

    print('draw a caption')
    t.penup()
    t.setpos(-(2*ht+wd), ht+wd+50)
    t.write('Pythagorean Theorem', font=('Arial', 18, 'normal'))
    t.setpos(-(2*ht+wd), ht+wd+25)
    t.write('Proof by construction: compass & straight edge:', font=('Arial', 14, 'normal'))
    t.home()

    # Move to initial location
    t.setpos(-(2*ht+wd), 0)

    print('draw initial triangle')
    r = t.pos()   # Save return point
    t.seth(east)
    t.pensize(thick)
    t.pencolor('black')
    t.fillcolor('light grey')
    t.pd()
    t.begin_fill()
    t.forward(wd)
    t.seth(north)
    t.forward(ht)
    t.pencolor('blue')
    t.pensize(thin)
    t.setpos(r)  # back to return point
    t.end_fill()

    # Add right angle marker:
    ## r = t.pos()  # Return point
    t.pensize(vthin)
    t.pencolor('black')
    t.penup()
    t.seth(east)
    t.forward(wd - 8)
    t.seth(north)
    t.pendown()
    t.forward(8)
    t.seth(east)
    t.forward(8)
    t.penup()
    t.setpos(r)  # Return

    print('triangle done')
    pause = raw_input('continue: ')

    print('construct first rectangle (first triangle clone)')
    t.pensize(thick)
    t.pencolor('black')
    t.fillcolor(pale_cyan)
    t.begin_fill()
    t.pendown()
    t.seth(north)
    t.forward(ht)
    t.pensize(thin)
    t.seth(east)
    t.forward(wd)
    t.end_fill()

    print('construct first square: b')
    # r = t.pos()
    t.fillcolor('pink')
    t.begin_fill()
    t.forward(ht)
    t.seth(south)
    t.pensize(thick)
    t.forward(ht)
    t.seth(west)
    t.forward(ht)
    t.penup()
    t.seth(north)
    t.forward(ht)
    t.end_fill()

    print('label first square: b')
    r = t.pos()
    t.seth(east)
    t.forward(ht/2)
    t.seth(south)
    t.forward(ht/2)
    t.write('b', font=('Arial', 13, 'italic'))
    t.setpos(r)


    print('construct second rectangle')
    t.seth(north)
    t.pensize(thin)
    t.fillcolor(pale_cyan)
    t.begin_fill()
    t.pendown()
    t.forward(wd)
    t.pensize(thick)
    r = t.pos()     # return for second hypotenuse/diagonal
    t.seth(east)
    t.forward(ht)
    t.seth(south)
    t.forward(wd)
    t.end_fill()
    t.pensize(thin)
    t.pencolor('blue')
    t.setpos(r)


    print('construct second square: a')
    t.fillcolor('pink')
    t.begin_fill()
    t.seth(west)
    t.pensize(thick)
    t.pencolor('black')
    t.forward(wd)
    t.seth(south)
    t.forward(wd)
    t.penup()
    t.seth(east)
    t.forward(wd)
    t.end_fill()

    print('label second square: a')
    r = t.pos()
    t.seth(west)
    t.forward(wd/2+5)
    t.seth(north)
    t.forward(wd/2-5)
    t.write('a', font=('Arial', 13, 'italic'))
    t.setpos(r)
    # Now turtle is located at bottom left (SE) corner of b square

    # Move turn to starting point for second enclosure
    t.penup()
    t.seth(east)
    t.forward(ht+thick)

    corners = list()
    # to save vetices of the inscribed
    # square as we build the enclosure
    corners.append(t.pos())

    print('construct second enclosure for "ring of triangles"')
    t.fillcolor(pale_cyan)
    t.begin_fill()
    t.pensize(thick)
    t.pencolor('red')
    t.pendown()
    t.seth(north)
    t.forward(wd)
    t.seth(east)
    t.forward(ht)
    corners.append(t.pos())
    t.forward(wd)
    t.seth(south)
    t.forward(ht)
    corners.append(t.pos())
    t.forward(wd)
    t.seth(west)
    t.forward(ht)
    corners.append(t.pos())
    t.forward(wd)
    t.seth(north)
    t.forward(ht)
    t.end_fill()
    t.penup()


    print('construct last (enclosed) square: c')
    t.fillcolor(lavender)
    t.begin_fill()
    t.pensize(thin)
    t.pencolor('blue')
    t.pendown()
    for each in corners:
        t.setpos(each)
    t.setpos(corners[0])
    t.end_fill()
    t.penup()

    print('label last (enclosed) square: c')
    t.pencolor('black')
    t.seth(east)
    t.forward((wd+ht)/2)
    t.seth(north)
    t.forward((wd+ht)/2 - ht)
    t.write('c', font=('Arial', 13, 'italic'))

    t.hideturtle()
    t.home()
    return w # XXX

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    save_diagram = False
    if len(args) == 3:
        try:
            import canvasvg
        except ImportError as e:
            print('Unable to import canvasvg: %s' % e, file=sys.stderr)
        else:
            save_diagram = args[2]
        args.pop()

    if len(args) < 2:
        print('Calling with default triangle size')
        height = 50
        width= 100
    else:
        try:
            args = [int(x) for x in args]
            height, width = args
        except ValueError as e:
            print('Unable to handle these dimensions', file=sys.stderr)
            print('Calling with default triangle size')

    screen = draw_diagram(height, width)
    if save_diagram:
        try:
            canvasvg.saveall(save_diagram, screen.getcanvas())
        except EnvironmentError, e:
            print('Unable to save diagram in file %s: %s' % (save_diagram, e),
              file=sys.stderr)
    turtle.mainloop()

