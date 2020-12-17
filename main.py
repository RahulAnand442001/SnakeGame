import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# objects
snake = Snake()
food = Food()
# get snake and food position
snake_position = ()
score_board = ScoreBoard()

# screen events
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    snake.move()

    # collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.update_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.game_over()

    # detect collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            score_board.game_over()

# screen will exit on click
screen.exitonclick()
