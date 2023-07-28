from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from time import sleep

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()
    sleep(.08)
    snake.move()

    if snake.head.distance(food) < 17:
        food.refresh()
        scoreboard.add_point()
        snake.increase_length()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()
