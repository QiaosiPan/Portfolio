"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT,
                            x=(window_width-paddle_width)/2, y=window_height-paddle_offset)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS*2, BALL_RADIUS*2,
                          x=window_width/2-BALL_RADIUS, y=window_height/2-BALL_RADIUS)
        self.ball.filled = True
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.rest_ball_velocity()

        # Initialize our mouse listeners
        self.live = 3
        self.gate = True
        onmousemoved(self.paddle_moving)
        onmouseclicked(self.start_game)

        # Draw bricks
        for i in range(0, BRICK_COLS):
            for j in range(0, BRICK_ROWS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT,
                                   x=i*(BRICK_WIDTH+BRICK_SPACING), y=BRICK_OFFSET+j*(BRICK_HEIGHT+BRICK_SPACING))
                self.brick.filled = True
                if j < BRICK_ROWS/5:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                elif BRICK_ROWS/5 <= j < BRICK_ROWS*2/5:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                elif BRICK_ROWS*2/5 <= j < BRICK_ROWS*3/5:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                elif BRICK_ROWS*3/5 <= j < BRICK_ROWS*4/5:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                elif BRICK_ROWS*4/5 <= j < BRICK_ROWS:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.window.add(self.brick)

    # Control paddle motion and it moving area
    def paddle_moving(self, mouse):
        # Let the center of paddle move with mouse.
        if PADDLE_WIDTH/2 <= mouse.x <= self.window.width-PADDLE_WIDTH/2:
            self.paddle.x = mouse.x - PADDLE_WIDTH/2
        # When mouse is outside the window, set the default paddle position. Avoid bug caused by mouse move too fast.
        elif mouse.x < PADDLE_WIDTH/2:
            self.paddle.x = 0
        elif mouse.x > self.window.width-PADDLE_WIDTH/2:
            self.paddle.x = self.window.width-PADDLE_WIDTH

    # Give initial velocity a random value
    def rest_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = - self.__dx

    # getter
    def get_ball_x_velocity(self):
        return self.__dx

    # getter
    def get_ball_y_velocity(self):
        return self.__dy

    # Animation loop
    def start_game(self, mouse):
        while True:
            # if live = 0, game is over
            if self.live <= 0:
                break
            # if gate = True, the game can be started by mouse click
            elif self.gate is True:
                self.gate = False
                self.live -= 1
                while True:
                    # detect if ball touch the wall, and reverse the __dx, __dy to bounce back
                    if self.ball_x_outside():
                        self.__dx = - self.__dx
                    if self.ball_top_outside():
                        self.__dy = - self.__dy
                    if self.ball_bott_outside():
                        self.ball.x = self.window.width / 2 - BALL_RADIUS
                        self.ball.y = self.window.height / 2 - BALL_RADIUS
                        self.rest_ball_velocity()
                        self.gate = True
                        break
                    # ball moving by __dx, __dy
                    self.ball.move(self.__dx, self.__dy)
                    # check if ball touches paddle or brick, and take actions
                    self.ball_touch()
                    pause(10)
            # if gate = False mean the mouse click during the game, do not execute anything.
            elif self.gate is False:
                pass

    # Definition of ball outside
    def ball_x_outside(self):
        is_ball_x_outside = (0 >= self.ball.x) or (self.ball.x >= self.window.width-BALL_RADIUS*2)
        return is_ball_x_outside

    def ball_top_outside(self):
        is_ball_top_outside = 0 >= self.ball.y
        return is_ball_top_outside

    def ball_bott_outside(self):
        is_ball_bott_outside = self.ball.y >= self.window.height-BALL_RADIUS*2
        return is_ball_bott_outside

    # The action when ball touch paddle or bricks
    def ball_touch(self):
        # definition of ball boundary coordinate
        maybe_obj1 = self.window.get_object_at(self.ball.x, self.ball.y)
        maybe_obj2 = self.window.get_object_at(self.ball.x, self.ball.y + BALL_RADIUS * 2)
        maybe_obj3 = self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y + BALL_RADIUS * 2)
        maybe_obj4 = self.window.get_object_at(self.ball.x + BALL_RADIUS * 2, self.ball.y)
        # check the ball is at brick area (brick area : upper than paddle)
        if self.ball.y < self.paddle.y-BALL_RADIUS * 2:
            # if one of coordinate touch the brick, remove the brick
            if maybe_obj1 is not None:
                self.window.remove(maybe_obj1)
                self.__dy = - self.__dy
            elif maybe_obj2 is not None:
                self.window.remove(maybe_obj2)
                self.__dy = - self.__dy
            elif maybe_obj3 is not None:
                self.window.remove(maybe_obj3)
                self.__dy = - self.__dy
            elif maybe_obj4 is not None:
                self.window.remove(maybe_obj4)
                self.__dy = - self.__dy
        # check the ball is at paddle area, and use the two coordinates at bottom to detect if ball touch paddle
        elif maybe_obj2 is not None:
            self.__dy = - self.__dy
        elif maybe_obj3 is not None:
            self.__dy = - self.__dy

