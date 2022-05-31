from turtle import Turtle, Screen
import random
import colorgram as c


screen = Screen()
screen.colormode(255)
timmy = Turtle()
timmy.up()
timmy.forward(-300)
timmy.left(90)
timmy.forward(-400)
timmy.right(90)
timmy.width(5)


picture = 'hist_spot_painting.jpg'


def colors_from_image(image):
    colors = c.extract(image, 30)
    l = []
    for color in colors:
        l.append(color.rgb)
    # retruns a list of tuples with colors: Rgb(r=248, g=248, b=245)
    return l

# Create an object of colors
specific_color = colors_from_image(picture)
length = len(specific_color)
rand_color = random.randint(0, length-1)


wide = 40
step = 20
def new_line(w, s):
    for _ in range(w):
        rand_color = random.randint(0, length - 1)
        timmy.pendown()
        timmy.dot(20, specific_color[rand_color])
        timmy.up()
        timmy.forward(s)


def back_to_new_line(w,s):
    timmy.left(90)
    timmy.up()
    timmy.forward(s)
    timmy.left(90)
    timmy.forward(s*w)
    timmy.left(180)


for _ in range(wide):
    new_line(wide,step)
    back_to_new_line(wide, step)


screen = Screen()
screen.exitonclick()