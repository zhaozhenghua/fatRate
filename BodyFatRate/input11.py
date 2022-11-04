import turtle as t

side = int(t.textinput(title="温馨提示",prompt="请输入正方形的边长"))
angle = 90

t.forward(side)

t.right(angle)
t.forward(side)

t.right(angle)
t.forward(side)

t.right(angle)
t.forward(side)

t.mainloop()