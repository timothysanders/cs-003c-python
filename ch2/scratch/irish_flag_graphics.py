from ezgraphics import GraphicsWindow

win = GraphicsWindow(700, 400)
canvas = win.canvas()
canvas.setColor("white")
canvas.setOutline("black")
canvas.drawRect(10, 10, 600, 300)
canvas.setColor(22, 155, 98)
canvas.drawRect(10, 10, 200, 300)
canvas.setColor(255, 136, 62)
canvas.drawRect(410, 10, 200, 300)
win.wait()
