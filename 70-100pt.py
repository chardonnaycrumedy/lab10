##########################################
#                                        #
#             Draw a house!              #
#                                        #
##########################################

# Use create_line(), create_rectangle() and create_oval() to make a 
# drawing of a house using the tKinter Canvas widget.

# 70pt: House outline (roof and the house)
# 80pt: Square windows and a door
# 90pt: A door handle plus a chimney!
# 100pt: Green grass on the ground and a red house!

# Minus 5pts if your code has no comments
# Minus 10pts if you only commit once to github

from Tkinter import *
root = Tk()

# Create the canvas widget
drawpad = Canvas(root, width=800,height=600, background='white')
drawpad.grid(row=0, column=1)

# Insert your code here to draw the house!

#house and roof
rectangle = drawpad.create_rectangle(200,200,400,400,fill="red")
line = drawpad.create_line(200,200,300,100,fill="red")
line = drawpad.create_line(300,100,400,200,fill="red")
line = drawpad.create_line(200,100,200,200,fill="red")
line = drawpad.create_line(200,100,220,100,fill="red")
line = drawpad.create_line(220,100,220,180,fill="red")
rectangle = drawpad.create_rectangle(180,400,420,420,fill="green")
#door
rectangle = drawpad.create_rectangle(270,390,320,320)
oval = drawpad.create_oval(310,350,320,360,fill="yellow")
#window
rectangle = drawpad.create_rectangle(220,220,280,260)
line = drawpad.create_line(250,220,250,260)
line = drawpad.create_line(220,240,280,240)

root.mainloop()