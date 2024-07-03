from ezgraphics import GraphicsWindow

win = GraphicsWindow(100, 100)
canvas = win.canvas()
canvas.drawLine(0, 25, 50, 25)
canvas.drawLine(25, 0, 25, 50)
canvas.drawLine(5, 5, 45, 45)
canvas.drawLine(5, 45, 45, 5)
win.wait()
