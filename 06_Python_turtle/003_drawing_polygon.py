import turtle


"""
t       :   turtle object
n       :   no. of sides of the polygon
length  :   length of every side

"""


def draw_polygon(t, n, length):
  angle = 360 / n
  for i in range(n):
    t.fd(length)
    t.lt(angle)
    
bob = turtle.Turtle()
draw_polygon(bob, 8, 100)

