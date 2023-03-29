"""
File: bouncing_ball.py
Name: QiaosiPan
-------------------------
"""

from campy.graphics.gobjects import GOval, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

# Global constants
VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')

# Create a ball
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
# asynchronous control variable
gate = True
# count times of ball bouncing
t = 1


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball)
    onmouseclicked(bouncing_start)


def bouncing_start(mouse):
    global gate, t
    vy = 0
    # check the bouncing status and the count of bouncing times
    # if gate is True, ball is ready for bouncing
    if gate is True and t <= 3:
        # close the gate, to avoid the ball bouncing again due to mouse clicking.
        gate = False
        t += 1
        # bouncing start
        while True:
            vy = vy + GRAVITY
            ball.move(3, vy)
            # bouncing finish if the ball is outside the window.
            if ball.x >= 800 and ball.y >= 500:
                # put the ball to the start point and wait for next click, the exit the while loop
                ball.x = START_X
                ball.y = START_Y
                break
            # if y>=500, ball touch the ground
            elif ball.y >= 500:
                # vy need to change direction and reduce
                vy = -vy*REDUCE
            pause(DELAY)
        gate = True
    # if mouse click when the ball is bouncing, do not execute anything.
    elif gate is False:
        pass
    # if mouse click more than 3 times, do not execute anything.
    elif t > 3:
        pass


if __name__ == "__main__":
    main()
