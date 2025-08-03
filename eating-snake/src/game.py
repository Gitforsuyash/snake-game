# src/game.py

import turtle
import random
from src import config
from utils.helper import update_score, reset_game, create_pen

def setup_screen():
    wn = turtle.Screen()
    wn.title("Snake Game by @TokyoEdtech")
    wn.bgcolor("green")
    wn.setup(width=600, height=600)
    wn.tracer(0)
    return wn

def create_head():
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("black")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"
    return head

def create_food():
    food = turtle.Turtle()
    food.speed(0)
    food.shape("circle")
    food.color("red")
    food.penup()
    food.goto(0, 100)
    return food

def create_segment():
    seg = turtle.Turtle()
    seg.speed(0)
    seg.shape("square")
    seg.color("grey")
    seg.penup()
    return seg

def move(head):
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

def handle_key_events(wn, head):
    wn.listen()
    wn.onkeypress(lambda: setattr(head, "direction", "up") if head.direction != "down" else None, "Up")
    wn.onkeypress(lambda: setattr(head, "direction", "down") if head.direction != "up" else None, "Down")
    wn.onkeypress(lambda: setattr(head, "direction", "left") if head.direction != "right" else None, "Left")
    wn.onkeypress(lambda: setattr(head, "direction", "right") if head.direction != "left" else None, "Right")
