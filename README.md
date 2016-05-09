Draw diagram for proving the Pythagorean Theorem
================================================

[[wiki/img/pythagorean_diagram1.png]]


Draws a diagram suitable for proving the Pythagorean Theorem
using turtle graphics..

It's possible to derive this diagram from any initial right triangle
using only a compass and straight edge; though this construction is
not yet used in the code.

This only exports one function `draw_diagram` taking two arguments, 
height, and width, and returning a reference to the (Turtle) screen
created by the function.  All constructions elements and labels/captions
are derived from those two arguments.

The return value of this function can be used to further play with the
resulting diagram.  To do this start a Python (2.x) or iPython
shell and issue the following commands:


```
>>> import pythy_turtle as pythy
>>> ## ... set height and width as desired: x and y
>>> screen = pythy.draw_diagram(x, y)
>>> turtle = screen.getturtles()[0]
```

As shown the single turtle used by this function can be obtained
for further manipuation from the object returned by the
`draw_diagram()` function.

To save the resulting image one can also use the canvasvg package
(https://pypi.python.org/pypi/canvasvg/1.0.0) like so:

```
>>> ## (given the preceding environment)
>>> import canvasvg
>>> ## Choose a filename
>>> cavasvg.save_all(filename, screen.getcanvas())
```

... ignore the warning about how canvasvg doesn't support images;
this code isn't using any of them and the exported SVG file looks
fine and converts easily to PDF or PNG.

When called as a standalone programm this code takes optional
command line arguments setting the height and width of the initial
triangle.  It does not control the size of the window opened by
the Turtle/Tk system; so the resulting diagram might not all be
visible and you may have to resize that window yourself.  Also
the function currently performs the drawing steps incrementally
and pauses for the user to hit [Enter] several times.  This is
an artifact of the interactive development process used to
write the code.  When the diagram is complete `__main__` calls
the Turtle.mainloop() function to allow the user to view and
manipulate the resulting window as desired.  Closing that window
will then drop out of `__main__`.

If a third command line argument is provided then it should be
a filename to which you want the resulting diagram to be saved
as an SVG (Scalable Vector Graphic).

If the program is called with arguments that cannot be converted
to Python integers then the default triangle height and width
(50x100) will be used.

Currently there are thick and thin lines, thick lines for outer
(enclosing) square edges, thin lines for inner edges.  Black for
the first (rectangular) enclosing square; red for the second
("ring of triangles") square.  The initial triangle is shaded
in light grey and has a customary "right angle" mark. The 
"a" and "b" squares are filled in pink; the "c" square is filled
in lavender; and the triangles are filled with a pale cyan.

This initial triangle is oriented in the manner customarily used
to draw a "unit circle" ... to facilitate associating these
related concepts.

Bugs and limitations:

* Uses console text and `raw_input` to step through the construction
   (This is currently tightly interlaced into the function; need to
   make that optional and decoupled).
* The steps used to draw the diagram do not show the hints necessary
   for c&s construction.  It's illustrative rather than being a proof.
* variable names in the function: w, t, wd, ht are horrible
   (they were used for the interactive session in which ai developed
   the code)
* Colors (line and fill) are hard-coded into the function
* Line thicknesses are hard-coded into the function
* No scaling nor translation/placement is done ... calling the draw
   function with strange arguments can 

To Do:
* Refactor the local variable names
* Offer iPython embedded shell option to call after image drawn
    (for use by programming students)
* Move interaction from console into Turtle/Tk events!
  * Add controls for ratio or height and width
  * Add better input validation and error messages
  * Add loop/option to clear canvas and do another drawing
  * Optional audio record/playback? (For video tutorial use)
* Add background image screen.bgpic()?  Greyed out portrait of
    Pythagoras?
* Use ratio option in lieu of absolute height/width
* (Optionally?) scale (custom) triangles to canvas size
* Add compass and straight edge sprites?
  * Animated?
* Port to JavaScript on HTML5 canvas and post to custom web
    page


