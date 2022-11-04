import random as r
import turtle as tu

# 设置画笔大小
tu.pensize(20)
tu.hideturtle()
tu.colormode(255)

tu.pencolor(
    r.randint(0,255),
    r.randint(0,255),
    r.randint(0,255)
)
tu.forward(100)



tu.pencolor(
    r.randint(0,255),
    r.randint(0,255),
    r.randint(0,255)
)
tu.right(90)
tu.forward(100)

tu.pencolor(
    r.randint(0,255),
    r.randint(0,255),
    r.randint(0,255)
)
tu.right(90)
tu.forward(100)


tu.pencolor(
    r.randint(0,255),
    r.randint(0,255),
    r.randint(0,255)
)
tu.right(90)
tu.forward(100)

tu.mainloop()