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
        self.paddle.color = 'tan'
        self.paddle.fill_color = 'tan'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS*2, BALL_RADIUS*2,
                          x=window_width/2-BALL_RADIUS, y=window_height/2-BALL_RADIUS)
        self.ball.filled = True
        self.ball.color = 'gray'
        self.ball.fill_color = 'slategray'
        self.window.add(self.ball)

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.rest_ball_velocity()

        # Initialize our mouse listeners
        self.live = 3
        self.score = 0
        self.gate = True
        onmousemoved(self.paddle_moving)
        onmouseclicked(self.start_game)
        text = "Live : " + str(self.live)
        self.label_live = GLabel(text)
        self.label_live.font = "SansSerif-22-bold"
        self.label_live.color = 'lightslategray'
        self.label_live_x = self.window.width - self.label_live.width - 10
        self.label_live_y = self.label_live.height*2
        self.window.add(self.label_live, self.label_live_x, self.label_live_y)
        text_score = "Score : " + str(self.score)
        self.label_score = GLabel(text_score)
        self.label_score.font = "SansSerif-22-bold"
        self.label_score.color = 'orangered'
        self.label_score_x = 10
        self.label_score_y = self.label_score.height * 2
        self.window.add(self.label_score, self.label_score_x, self.label_score_y)

        # Draw bricks
        # self.color = ['red', 'orange', 'yellow', 'green', 'blue']
        self.color = ['darkred', 'darksalmon', 'khaki', 'darkseagreen', 'steelblue']
        for i in range(0, BRICK_COLS):
            for j in range(0, BRICK_ROWS):
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT,
                                   x=i*(BRICK_WIDTH+BRICK_SPACING), y=BRICK_OFFSET+j*(BRICK_HEIGHT+BRICK_SPACING))
                self.brick.filled = True
                self.brick.fill_color = self.color[int(j/2 % 5)]
                self.brick.color = self.color[int(j/2 % 5)]
                self.window.add(self.brick)

        # Draw hint
        self.label_start = GLabel("CLICK TO START")
        self.label_start.font = "SansSerif-36-bold"
        self.label_start.color = 'yellowgreen'
        self.label_start_x = (self.window.width - self.label_start.width) / 2
        self.label_start_y = 1.7 * (self.window.height + self.label_start.ascent) / 3
        self.window.add(self.label_start, self.label_start_x, self.label_start_y)
        self.label_end = GLabel("GAME OVER")
        self.label_end.font = "SansSerif-36-bold"
        self.label_end.color = 'tomato'
        self.label_end_x = (self.window.width - self.label_end.width) / 2
        self.label_end_y = 1.7 * (self.window.height + self.label_end.ascent) / 3
        self.label_win = GLabel("YOU WIN ^O^/")
        self.label_win.font = "SansSerif-36-bold"
        self.label_win.color = 'tomato'
        self.label_win_x = (self.window.width - self.label_win.width) / 2
        self.label_win_y = 1.7 * (self.window.height + self.label_win.ascent) / 3

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
        if self.gate is True:
            self.window.remove(self.label_start)
            self.ball_bouncing()
        else:
            pass

    def ball_bouncing(self):
        # if gate = True, the game can be started by mouse click
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
                # self.rest_ball_velocity()
                self.gate = True
                text = 'Live : ' + str(self.live)
                self.label_live.text = text
                # if live = 0, game is over
                if self.live == 0:
                    self.gate = False
                    self.window.add(self.label_end, self.label_end_x, self.label_end_y)
                else:
                    self.window.add(self.label_start, self.label_start_x, self.label_start_y)
                break
            # ball moving by __dx, __dy
            self.ball.move(self.__dx, self.__dy)
            # check if ball touches paddle or brick, and take actions
            self.ball_touch()
            if self.score == 100:
                self.gate = False
                self.window.add(self.label_win, self.label_win_x, self.label_win_y)
                break
            pause(13)

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
            if self.ball.y <= BRICK_OFFSET:
                self.__dy = - self.__dy
            elif maybe_obj1 is not None:
                self.window.remove(maybe_obj1)
                self.score += 1
                self.speedup()
                self.__dy = - self.__dy
            elif maybe_obj2 is not None:
                self.window.remove(maybe_obj2)
                self.score += 1
                self.speedup()
                self.__dy = - self.__dy
            elif maybe_obj3 is not None:
                self.window.remove(maybe_obj3)
                self.score += 1
                self.speedup()
                self.__dy = - self.__dy
            elif maybe_obj4 is not None:
                self.window.remove(maybe_obj4)
                self.score += 1
                self.speedup()
                self.__dy = - self.__dy
            text_score = "Score : " + str(self.score)
            self.label_score.text = text_score
        # check the ball is at paddle area, and use the two coordinates at bottom to detect if ball touch paddle
        elif (maybe_obj2 is not None and maybe_obj2 != self.label_live and maybe_obj2 != self.label_score) or \
                (maybe_obj3 is not None and maybe_obj3 != self.label_live and maybe_obj3 != self.label_score):
            self.__dy = - self.__dy

    def speedup(self):
        if self.score == 5:
            self.__dx *= 1.1
            self.__dy *= 1.1
        elif self.score == 20:
            self.__dx *= 1.05
            self.__dy *= 1.05
        elif self.score == 40:
            self.__dx *= 1.1
            self.__dy *= 1.1
        elif self.score == 80:
            self.__dx *= 1.1
            self.__dy *= 1.1

