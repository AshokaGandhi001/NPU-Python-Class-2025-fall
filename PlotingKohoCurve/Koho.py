import turtle

# 递归绘制科赫曲线
def koch_curve(t, length, order):
    if order == 0:
        t.forward(length)
    else:
        length /= 3
        koch_curve(t, length, order - 1)
        t.left(60)
        koch_curve(t, length, order - 1)
        t.right(120)
        koch_curve(t, length, order - 1)
        t.left(60)
        koch_curve(t, length, order - 1)

# 主绘图函数
def main():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)     # 调到最快
    t.pensize(2)

    # 起始位置
    t.penup()
    t.goto(-200, 50)
    t.pendown()

    # 绘制 4 阶科赫曲线
    koch_curve(t, 400, 3)
    t.right(120)
    koch_curve(t, 400, 3)
    t.right(120)
    koch_curve(t, 400, 3)
    t.right(120)

    turtle.done()

if __name__ == "__main__":
    main()
