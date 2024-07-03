from ezgraphics import GraphicsWindow

win = GraphicsWindow(400, 400)
canvas = win.canvas()
xLeft = 10
yTop = 10
canvas.setColor("black")
canvas.drawRect(xLeft, yTop, 50, 150)
canvas.setColor("red")
canvas.drawOval(xLeft + 5, yTop + 5, 40, 40)
canvas.setColor("yellow")
canvas.drawOval(xLeft + 5, yTop + 55, 40, 40)
canvas.setColor("green")
canvas.drawOval(xLeft + 5, yTop + 105, 40, 40)
win.wait()
