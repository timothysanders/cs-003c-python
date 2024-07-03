from ezgraphics import GraphicsWindow

win = GraphicsWindow(400, 400)
canvas = win.canvas()
canvas.drawOval(150, 150, 200, 200)
win.wait()
