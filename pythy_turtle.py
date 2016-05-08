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

    east = 0
    north = 90
    west = 180
    south = 270
    thick = 4
    thin = 2

    pale_cyan = '#88F4F0'
    lavender  = '#F388D7'

    print('draw a caption')
    t.penup()
    t.setpos(-(2*ht+wd), ht+wd+50)
    t.write('Pythagorean Theorem', font=('Arial', 18, 'normal'))
    t.setpos(-(2*ht+wd), ht+wd+25)
    t.write('Proof by construction: compass & straight edge:', font=('Arial', 14, 'normal'))
    t.home()

    print('draw a triangle')
    t.seth(north)
    t.pensize(thick)
    t.pd()
    t.fillcolor('cyan')
    t.begin_fill()
    t.forward(ht)
    t.pencolor('blue')
    t.pensize(thin)
    t.setpos(wd, 0)
    t.seth(west)
    t.pencolor('black')
    t.pensize(thick)
    t.forward(wd)
    t.end_fill()

    # Add right angle marker:
    t.pensize(thin)
    t.pencolor('black')
    r = t.pos()  # Return point
    t.penup()
    t.seth(east)
    t.forward(10)
    t.seth(north)
    t.pendown()
    t.forward(10)
    t.seth(west)
    t.forward(10)
    t.penup()
    t.setpos(r)  # Return

    print('triangle done')
    pause = raw_input('continue: ')

    print('construct square from height')
    t.pensize(thick)
    t.pencolor('black')
    t.fillcolor('pink')
    t.pendown()
    t.begin_fill()
    t.forward(ht)
    t.seth(north)
    t.pensize(thick)
    t.pencolor('yellow')
    t.forward(ht)
    t.seth(east)
    t.pensize(thin)
    t.pencolor('grey')
    t.forward(ht)
    t.end_fill()
    print('height square done')
    pause = raw_input('continue: ')

    print('construct congruent triangle off original')
    t.pensize(thin)
    t.pencolor('grey')
    t.fillcolor(pale_cyan)
    r = t.pos() # return point for this triangle
    t.begin_fill()
    t.forward(wd)
    t.seth(south)
    t.pensize(thick)
    t.pencolor('black')
    t.forward(ht)
    t.pensize(thin)
    t.pencolor('blue')
    t.setpos(r)
    t.end_fill()
    print('congruent triangle done')
    pause = raw_input('continue: ')

    print('construct congruent rectangle')
    t.pensize(thin)
    t.pencolor('grey')
    t.seth(north)
    t.forward(wd)
    r = t.pos() # return point for this triangle
    t.pensize(thick)
    t.pencolor('black')
    t.fillcolor(pale_cyan)
    t.begin_fill()
    t.seth(west)
    t.forward(ht)
    t.seth(south)
    t.pensize(thick)
    t.pencolor('yellow')
    t.forward(wd)
    t.pensize(thin)
    t.pencolor('blue')
    t.setpos(r)
    t.end_fill()
    print('congruent rectangle done')
    pause = raw_input('continue: ')

    print('construct width square')
    t.fillcolor('pink')
    t.pensize(thick)
    t.pencolor('black')
    t.begin_fill()
    t.seth(east)
    t.forward(wd)
    t.seth(south)
    t.forward(wd)
    t.pensize(thin)
    t.pencolor('grey')
    t.seth(west)
    t.forward(wd)
    t.end_fill()
    print('width square done')
    pause = raw_input('continue: ')


    print('This large square consists of two smaller squares and four identically sized triangles')
    print('The two small squares are the height and width')
    pause = raw_input('continue: ')
    print('Now we construct another large square from the existing large squared (filled with lavender)')
    pause = raw_input('continue: ')

    print('construct second large square')
    r = list() # list of return points for inner square
    t.penup()
    t.home()
    t.seth(west)
    t.forward(ht) # bottom left corner of first large square
    t.begin_fill()
    t.pensize(thick)
    t.pencolor('red')
    t.pendown()
    t.fillcolor(pale_cyan)
    t.forward(wd)
    r.append(t.pos()) # save first return point
    t.forward(ht)
    t.seth(north)
    t.forward(wd)
    r.append(t.pos()) # save second return point
    t.forward(ht)
    t.seth(east)
    t.forward(wd)
    r.append(t.pos()) # save third return point 
    t.forward(ht)
    t.end_fill()
    t.pencolor('red')
    t.penup()
    print('second large square done')
    pause = raw_input('continue: ')

    print('construct "ring" of congruent triangles')
    t.pensize(thin)
    t.pencolor('blue')
    t.fillcolor(lavender)
    t.seth(south)
    t.begin_fill()
    t.forward(wd)
    t.pensize(thick)
    t.pencolor('yellow')
    r.append(t.pos()) # save starting point
    t.pendown()
    t.pensize(thin)
    t.pencolor('blue')
    for each in r:
        # draw lines to each of our points and back to start
        t.setpos(each)  
    print('"ring" of congruent triangles done')
    pause = raw_input('continue: ')


    print('Finish divider between two large squares')
    t.end_fill()
    t.pensize(thick)
    t.pencolor('yellow')
    t.seth(south)
    t.forward(ht)
    print('Fill in last copy of triangle')
    t.penup()
    t.setpos(r[-1])
    t.pensize(thin)
    t.pencolor('grey')
    t.fillcolor(pale_cyan)
    t.begin_fill()
    t.seth(east)
    t.forward(ht)
    t.seth(north)
    t.forward(wd)
    t.end_fill()
    t.pencolor('blue')
    print('Add labels to squares: a, b, and c')
    t.setpos(-(ht/2), (ht/2))
    t.write('a', font=('Arial', 13, 'italic'))
    t.setpos((wd/2), ht+(wd/2))
    t.write('b', font=('Arial', 13, 'italic'))
    t.setpos(-((wd+ht)/2+ht), (wd+ht)/2)
    t.write('c', font=('Arial', 13, 'italic'))

    t.setpos(r[-1]) # Back to starting point for inner square
    t.hideturtle()
    print('Done')
    pause = raw_input('continue: ')
    return w

if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
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
    screen.mainloop()

