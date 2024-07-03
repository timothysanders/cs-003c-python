from ezgraphics import GraphicsWindow

win = GraphicsWindow(400, 400)
canvas = win.canvas()
canvas.setOutline("red")
canvas.drawText(50, 50, "red")
canvas.setOutline("green")
canvas.drawText(50, 100, "green")
canvas.setOutline("blue")
canvas.drawText(50, 150, "blue")
win.wait()
