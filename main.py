from turtle import getscreen
import time
from snake import snake
from food import Food
from scoreboard import scoreboard

screen = getscreen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("the snake game")
screen.tracer(0)

snake = snake()
food = Food()
scoreboard = scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        scoreboard.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 280 or snake.head.ycor() < - 280:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()

