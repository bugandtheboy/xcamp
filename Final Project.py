import turtle as t
s=t.Screen()
t.speed(0)
s.bgcolor("green yellow")
t.pencolor("dark violet")
s.setup(1900,1300)
t.penup()
t.goto(-935,580)
t.pendown()
t.write("Use the begining letter of each word to make the shape it can make a hexagon,pentagon,instuctions,triangle,and circle.")
t.right(90)
t.penup()
t.forward(20)
t.pendown()
t.write("For penup click u, for pendown click d, arrow keys for movement,q for square,and finally click x to clear, remember when you clear the instuctions will clear too.")
t.penup()
t.forward(20)
t.pendown()
t.write("Use s for small shapes and l for large ones")
t.pendown()
x=1.0

def instructions():
    t.penup()
    t.goto(-935,580)
    t.write("Use the begining letter of each word to make the shape it can make a hexagon,pentagon,instuctions,triangle,and circle.")
    t.right(90)
    t.penup()
    t.forward(20)
    t.pendown()
    t.write("For penup click u, for pendown click d, arrow keys for movement,q for square,and finally click x to clear, remember when you clear the instuctions will clear too.")
    t.penup()
    t.forward(20)
    t.pendown()
    t.write("Use s for small shapes and l for large ones")
    t.pendown()
def small():
    global x
    x=0.5
def medium():
    global x
    x=1.0 
def large():
    global x
    x=2
def draw_triangle():
    t.forward(60*x)
    t.left(135)
    t.forward(40*x)
    t.left(90)
    t.forward(40*x)
    t.left(135)
def draw_square():
    for p in range(4):
        t.forward(40*x)
        t.left(90)
        p+=1
def draw_circle():
    t.circle(20*x)
def draw_pentagon():
    for i in range(5):
        t.forward(40*x)
        t.left(72)
        i+=1
def draw_hexagon():
    for r in range(6):
        t.forward(40*x)
        t.left(60)
        r+=1
def forwards():
    t.forward(10)
def backwards():
    t.backward(10)
def lefts():
    t.left(90)
def rights():
    t.right(90)
def penup_t():
    t.penup()
def pendown_t():
    t.pendown()
def clear():
    t.clear()
def pen(l,k):
    t.goto(l,k)
t.hideturtle()
t.onscreenclick(pen)
t.showturtle()
s.onkeypress(draw_square,"q")
s.onkeypress(draw_circle,"c")
s.onkeypress(draw_triangle,"t")
s.onkeypress(draw_pentagon,"p")
s.onkeypress(draw_hexagon,"h")
s.onkeypress(forwards,"Up")
s.onkeypress(backwards,"Down")
s.onkeypress(lefts,"Left")
s.onkeypress(rights,"Right")
s.onkeypress(penup_t,"u")
s.onkeypress(pendown_t,"d")
s.onkeypress(clear,"x")
s.onkeypress(instructions,"i")
s.onkeypress(small,"s")
s.onkeypress(medium,"m")
s.onkeypress(large,"l")
s.listen()
