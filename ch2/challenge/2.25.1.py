from ezgraphics import GraphicsWindow

win = GraphicsWindow(400, 400)
canvas = win.canvas()
canvas.drawRect(0, 5, 20, 30)
canvas.drawRect(0, 5, 40, 60)
canvas.drawRect(20, 35, 20, 30)
win.wait()
