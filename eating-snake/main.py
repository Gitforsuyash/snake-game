# main.py

import time
import random
from src import config
from src.game import setup_screen, create_head, create_food, create_segment, move, handle_key_events
from utils.helper import update_score, reset_game, create_pen

def run_game():
    wn = setup_screen()
    head = create_head()
    food = create_food()
    pen = create_pen()
    segments = []

    handle_key_events(wn, head)
    update_score(pen, config.score, config.high_score)

    while True:
        wn.update()

        if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
            reset_game(head, segments, pen, config)

        if head.distance(food) < 20:
            food.goto(random.randint(-290, 290), random.randint(-290, 290))
            segments.append(create_segment())
            config.delay -= 0.001
            config.score += 10
            config.high_score = max(config.high_score, config.score)
            update_score(pen, config.score, config.high_score)

        for i in range(len(segments) - 1, 0, -1):
            segments[i].goto(segments[i - 1].pos())

        if segments:
            segments[0].goto(head.pos())

        move(head)

        for segment in segments:
            if segment.distance(head) < 20:
                reset_game(head, segments, pen, config)
                break

        time.sleep(config.delay)

if __name__ == "__main__":
    run_game()
