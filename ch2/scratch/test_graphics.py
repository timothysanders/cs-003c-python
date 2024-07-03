from ezgraphics import GraphicsWindow

win = GraphicsWindow()
canvas = win.canvas()

canvas.setColor("red")
canvas.drawRect(15, 10, 20, 30)
canvas.drawOval(10, 10, 30, 30)

win.wait()
