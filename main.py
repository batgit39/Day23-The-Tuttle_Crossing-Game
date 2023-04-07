import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("The Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

score = Scoreboard()
player = Player()
car = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")


x = 0.01
game_is_on = True
while game_is_on:
    time.sleep(x)


    if player.ycor() > 280:
        score.update_score()
        player.start_over()
        x *= 0.9 

    random_number = random.randint(1, 5)
    if random_number == 3:
        car.new_car() 

    car.car_move()
    screen.update()

    for i in car.car_list:
        if i.distance(player) < 20:
            game_is_on = False
