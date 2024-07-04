# CS03C Lab 3 - 2.27.31
# Zoe Rodriguez and Tim Sanders
# 7/3/2024

from ezgraphics import GraphicsWindow

GOLDEN_GATE_SPAN_FEET = 4200
BROOKLYN_SPAN_FEET = 1595
DELAWARE_MEMORIAL_SPAN_FEET = 2150
MACKINAC_SPAN_FEET = 3800

# Calculate appropriate pixel widths
goldenGateSpanPixels = GOLDEN_GATE_SPAN_FEET / 10
brooklynSpanPixels = BROOKLYN_SPAN_FEET / 10
delawareSpanPixels = DELAWARE_MEMORIAL_SPAN_FEET / 10
mackinacSpanPixels = MACKINAC_SPAN_FEET / 10

# Create overall GraphicsWindow and canvas
win = GraphicsWindow(width=600, height=500)
canvas = win.canvas()

# Draw overall container for bar chart
canvas.drawRect(x=10, y=20, width=500, height=400)

# Add scale markings for every five hundred feet of bridge span
canvas.drawLine(x1=60, y1=420, x2=60, y2=415)
canvas.drawLine(x1=110, y1=420, x2=110, y2=415)
canvas.drawLine(x1=160, y1=420, x2=160, y2=415)
canvas.drawLine(x1=210, y1=420, x2=210, y2=415)
canvas.drawLine(x1=260, y1=420, x2=260, y2=415)
canvas.drawLine(x1=310, y1=420, x2=310, y2=415)
canvas.drawLine(x1=360, y1=420, x2=360, y2=415)
canvas.drawLine(x1=410, y1=420, x2=410, y2=415)
canvas.drawLine(x1=460, y1=420, x2=460, y2=415)

# Create bars for each bridge
# Golden Gate Bridge
canvas.setColor(red=181, green=51, blue=51)
canvas.drawRect(x=10, y=32.5, width=goldenGateSpanPixels, height=75)

# Brooklyn Bridge
canvas.setColor("green")
canvas.drawRect(x=10, y=132.5, width=brooklynSpanPixels, height=75)

# Delaware Memorial Bridge
canvas.setColor("blue")
canvas.drawRect(x=10, y=232.5, width=delawareSpanPixels, height=75)

# Mackinac Bridge
canvas.setColor("grey")
canvas.drawRect(x=10, y=332.5, width=mackinacSpanPixels, height=75)

# Add text labels
canvas.setColor("black")
canvas.drawText(x=200, y=10, text="Lab 2.27.31: Bridge Span Bar Chart")
canvas.drawText(x=250, y=450, text="Span in feet")
canvas.drawText(x=50, y=425, text="500")
canvas.drawText(x=100, y=425, text="1000")
canvas.drawText(x=150, y=425, text="1500")
canvas.drawText(x=200, y=425, text="2000")
canvas.drawText(x=250, y=425, text="2500")
canvas.drawText(x=300, y=425, text="3000")
canvas.drawText(x=350, y=425, text="3500")
canvas.drawText(x=400, y=425, text="4000")
canvas.drawText(x=450, y=425, text="4500")
canvas.drawText(x=15, y=65, text="Golden Gate Bridge: %d ft" % GOLDEN_GATE_SPAN_FEET)
canvas.drawText(x=15, y=165, text="Brooklyn Bridge: %d ft" % BROOKLYN_SPAN_FEET)
canvas.drawText(x=15, y=265, text="Delaware Memorial Bridge: %d ft" % DELAWARE_MEMORIAL_SPAN_FEET)
canvas.drawText(x=15, y=365, text="Mackinac Bridge: %d ft" % MACKINAC_SPAN_FEET)

win.wait()
