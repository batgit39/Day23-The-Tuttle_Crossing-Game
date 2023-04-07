from turtle import Turtle, width
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
# y_axis = (300,   )
STARTING_POSITION = (340, random.randint(0,300)) 
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_list = []


    def new_car(self):
        car = Turtle("square") 
        car.penup()
        car.turtlesize(stretch_wid = 1, stretch_len = 2)       
        car.color(random.choice(COLORS))
        self.new_position(car)
        self.car_list.append(car)

    def car_move(self):
        for i in self.car_list:
            i.backward(STARTING_MOVE_DISTANCE)

    def new_position(self, car):
        interval = random.randint(-12,12)
        y = interval * 20 
        x = 340 + interval
        car.goto(x, y)
