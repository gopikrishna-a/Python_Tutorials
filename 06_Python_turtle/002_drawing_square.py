import turtle


#creating function to draw a square
def draw_square(t):
  for i in range(4):
    t.fd(100)
    t.lt(90)  #value in degree (arrow movement direction)

bob = turtle.Turtle()
draw_square(bob)

#output wil be a square diagram






