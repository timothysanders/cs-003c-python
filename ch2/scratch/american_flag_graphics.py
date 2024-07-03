from ezgraphics import GraphicsWindow

win = GraphicsWindow()
canvas = win.canvas()
canvas.setColor("white")
canvas.setOutline("black")
canvas.drawRect(10, 10, 190, 100)
canvas.setColor(0, 38, 100)
canvas.drawRect(10, 10, 76, 54)
canvas.setColor(177, 35, 50)
canvas.drawRect(87, 10, 113, 7.7)
canvas.drawRect(87, 25, 113, 7.7)
canvas.drawRect(87, 40, 113, 7.7)
canvas.drawRect(87, 56, 113, 7.7)
canvas.drawRect(10, 71, 190, 7.7)
canvas.drawRect(10, 86, 190, 7.7)
canvas.drawRect(10, 102, 190, 7.7)
canvas.drawLin
win.wait()
