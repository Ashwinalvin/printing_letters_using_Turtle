import turtle
li=['a','b','d']
def cap(li,n,m):
  for i in li:
    if i=='a':
      t = turtle.Turtle()
      t.shape('circle')
      t.color('green', 'green')
      t.pensize(20)
      t.speed(0)
      t.up()
      t.goto(n+50,m)
      t.down()
      t.left(60)
      t.forward(200)
      t.right(120)
      t.forward(200)
      t.up()
      t.goto(n+50,m)
      t.setheading(0)
      t.down()
      t.left(60)
      t.forward(100)
      t.right(60)
      t.forward(100)
      n=n+250
    if i=='b':
      t = turtle.Turtle()
      t.shape('circle')
      t.color('green', 'green')
      t.pensize(20)
      t.speed(0)
      t.up()
      t.goto(n+50,m) #to avoid over lapping between letters
      t.down()
      t.setheading(0)
      t.left(90)
      t.forward(200)
      t.right(90)
      t.circle(-50,180)
      t.right(180)
      t.circle(-50,180)
      n=n+200
    if i == 'c':
      t = turtle.Turtle()
      t.color('green', 'green')
      t.shape('circle')
      t.pensize(20)
      t.speed(1)
      t.up()
      t.goto(n+50, m)  # to avoid over lapping between letters
      t.down()
      t.setheading(0)
      t.left(180)
      t.circle(-100, 180)
      n = n+100

    if i=='d':
        t = turtle.Turtle()
        t.color('green', 'green')
        t.shape('circle')
        t.pensize(20)
        t.speed(1)
        t.up()
        t.goto(n + 50, m)  # to avoid over lapping between letters
        t.down()
        t.setheading(0)
        t.left(90)
        t.forward(200)
        t.right(90)
        t.circle(-100, 180)
        n = n+100
    if i=='e':
        t = turtle.Turtle()
        t.color('green', 'green')
        t.shape('circle')
        t.pensize(20)
        t.speed(1)
        t.up()
        t.goto(n + 50, m)  # to avoid over lapping between letters
        t.down()
        t.setheading(0)
        t.left(90)
        t.forward(200)
        t.right(90)
        t.forward(50)
        t.backward(50)
        t.right(90)
        t.forward(100)
        t.setheading(0)
        t.forward(50)
        t.backward(50)
        t.right(90)
        t.forward(100)
        t.setheading(0)
        t.forward(50)
        n = n+100
    if i=='f':
        t = turtle.Turtle()
        t.color('green', 'green')
        t.shape('circle')
        t.pensize(20)
        t.speed(1)
        t.up()
        t.goto(n + 50, m)  # to avoid over lapping between letters
        t.down()
        t.setheading(0)
        t.left(90)
        t.forward(200)
        t.right(90)
        t.forward(50)
        t.backward(50)
        t.right(90)
        t.forward(100)
        t.setheading(0)
        t.forward(50)
        t.backward(50)




















cap(li,-200,0)





