# utils/helpers.py

import time
from turtle import Turtle

def create_pen():
    pen = Turtle()
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    return pen

def update_score(pen, score, high_score):
    pen.clear()
    pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

def reset_game(head, segments, pen, config):
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"

    for segment in segments:
        segment.goto(1000, 1000)
    segments.clear()

    config.score = 0
    config.delay = 0.1
    update_score(pen, config.score, config.high_score)
