import turtle

# task 2:
def koch_curve(t, order, size):
  if order == 0:
      t.forward(size)
  else:
      for angle in [60, -120, 60, 0]:
          koch_curve(t, order - 1, size / 3)
          t.left(angle)

def draw_koch_curve(order, size=300):
  window = turtle.Screen()
  window.setup(width=800, height=800)
  window.bgcolor("white")

  t = turtle.Turtle()
  t.speed(0)
  t.penup()
  t.goto(-size / 2, size / 3)
  t.pendown()
  t.color("blue")

  for _ in range(3):
      koch_curve(t, order, size)
      t.right(120)

  turtle.done()

draw_koch_curve(2)