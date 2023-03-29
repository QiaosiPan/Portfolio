"""
File: my_drawing.py
Name: QiaosiPan
----------------------
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon, GArc
from campy.graphics.gwindow import GWindow

width = 850
height = 750
window = GWindow(width=width, height=height, title='Kirby')


def main():
    """
    File: Kirby on the Cloud Castle

    Kirby's life on the cloud castle is quite peace and happy,
    except when he is hungry. 0_0
    """
    # background
    background()
    # create castle
    castle(-10, 450)
    castle(70, 50)
    castle(370, 480)
    castle(450, 120)
    castle(700, 20)
    # create hungry Kirby
    x1, y1 = 80, 300                        # position of Kirby (all elements will follow this coordinate)
    make_a_kirby(x1, y1)                    # create a Kirby without mouth
    make_eating_mouth(x1, y1)               # create a eating mouth
    kirby_name(x1, y1, 'Kirby is hungry!')  # create a label
    # create happy Kirby
    x2, y2 = 480, 300                       # position of Kirby (all elements will follow this coordinate)
    make_a_kirby(x2, y2)                    # create a Kirby without mouth
    make_smile_mouth(x2, y2)                # create a smile mouth
    kirby_name(x2, y2, 'Kirby is Happy!')   # create a label


# function of background


def background():
    # Create blue background : sky
    rect = GRect(850, 750)
    rect.filled = True
    rect.color = 'lightskyblue'
    rect.fill_color = 'lightskyblue'
    window.add(rect)
    # Create cloud on the ground
    for i in range(0, 4):
        circle = GOval(450, 300, x=-250+i*250, y=550)
        circle.filled = True
        circle.color = 'white'
        circle.fill_color = 'white'
        window.add(circle)


def castle(x, y):
    roof = GPolygon()
    roof.add_vertex((50, 30))
    roof.add_vertex((0, 30))
    roof.add_vertex((25, 0))
    roof.filled = True
    roof.color = 'maroon'
    roof.fill_color = 'maroon'
    rect = GRect(30, 60)
    rect.filled = True
    rect.color = 'lightgrey'
    rect.fill_color = 'lightgrey'
    glass = GRect(15, 15)
    glass.filled = True
    glass.color = 'lightblue'
    glass.fill_color = 'seashell'
    for i in range(0, 2):
        circle = GOval(50, 40, x=0+i*40+x, y=95+y)
        circle.filled = True
        circle.color = 'white'
        circle.fill_color = 'white'
        window.add(circle)
    circle1 = GOval(60, 60, x=15+x, y=80+y)
    circle1.filled = True
    circle1.color = 'white'
    circle1.fill_color = 'white'
    circle2 = GOval(10, 10, x=-12+x, y=115+y)
    circle2.filled = True
    circle2.color = 'white'
    circle2.fill_color = 'white'
    circle3 = GOval(5, 5, x=-18+x, y=120+y)
    circle3.filled = True
    circle3.color = 'white'
    circle3.fill_color = 'white'
    window.add(circle1)
    window.add(circle2)
    window.add(circle3)
    window.add(rect, x=30+x, y=52+y)
    window.add(roof, x=20+x, y=28+y)
    window.add(glass, x=38+x, y=70+y)


# main function of drawing a Kirby body & its emotion


def kirby_name(x, y, name):
    # draw the label
    label = GLabel(str(name), x=x, y=y+400)
    label.font = 'Helvetica-40-bold'
    label.color = 'slategray'
    window.add(label)


def make_smile_mouth(x, y):
    # create Kirby's smile mouth
    mouth = GArc(60, 270, 210, 120)
    window.add(mouth, x=125+x, y=110+y)


def make_eating_mouth(x, y):
    # create Kirby's eating mouth
    mouth = make_mouth(60+x, 148+y)
    tongue = make_tongue(75+x, 205+y)
    window.add(mouth)
    window.add(tongue)


def make_a_kirby(x, y):
    # Combine all the element on Kirby
    # Body element
    body = make_body(0+x, 0+y)
    hand_r = make_hand(250+x, 100+y)
    hand_l = make_hand(-50+x, 100+y)
    feet_r = make_feet(175+x, 265+y)
    feet_l = make_feet(-15+x, 265+y)
    # face element
    eye1_r = make_eye1(170+x, 60+y)
    eye1_l = make_eye1(90+x, 60+y)
    eye2_r = make_eye2(175+x, 60+y)
    eye2_l = make_eye2(95+x, 60+y)
    eye3_r = make_eye3(173+x, 98+y)
    eye3_l = make_eye3(93+x, 98+y)
    eye4_r = make_eye4(173+x, 90+y)
    eye4_l = make_eye4(93+x, 90+y)
    cheek_r = make_cheek(205+x, 135+y)
    cheek_l = make_cheek(25+x, 135+y)
    # put elements on the window
    window.add(feet_r)
    window.add(feet_l)
    window.add(hand_r)
    window.add(hand_l)
    window.add(body)
    window.add(eye1_r)
    window.add(eye1_l)
    window.add(eye3_r)
    window.add(eye3_l)
    window.add(eye4_r)
    window.add(eye4_l)
    window.add(eye2_r)
    window.add(eye2_l)
    window.add(cheek_r)
    window.add(cheek_l)


# function of element on Kirby's body & face


def make_eye1(x, y):
    obj = GOval(40, 90, x=x, y=y)
    obj.color = 'black'
    obj.filled = True
    obj.fill_color = 'black'
    return obj


def make_eye2(x, y):
    obj = GOval(30, 45, x=x, y=y)
    obj.color = 'white'
    obj.filled = True
    obj.fill_color = 'white'
    return obj


def make_eye3(x, y):
    obj = GOval(35, 50, x=x, y=y)
    obj.color = 'blue'
    obj.filled = True
    obj.fill_color = 'blue'
    return obj


def make_eye4(x, y):
    obj = GOval(35, 35, x=x, y=y)
    obj.color = 'black'
    obj.filled = True
    obj.fill_color = 'black'
    return obj


def make_mouth(x, y):
    obj = GOval(180, 150, x=x, y=y)
    obj.color = 'red'
    obj.filled = True
    obj.fill_color = 'red'
    return obj


def make_tongue(x, y):
    obj = GOval(150, 90, x=x, y=y)
    obj.color = 'salmon'
    obj.filled = True
    obj.fill_color = 'salmon'
    return obj


def make_cheek(x, y):
    obj = GOval(70, 30, x=x, y=y)
    obj.color = 'hotpink'
    obj.filled = True
    obj.fill_color = 'hotpink'
    return obj


def make_feet(x, y):
    obj = GOval(150, 60, x=x, y=y)
    obj.color = 'hotpink'
    obj.filled = True
    obj.fill_color = 'hotpink'
    return obj


def make_hand(x, y):
    obj = GOval(90, 60, x=x, y=y)
    obj.color = 'pink'
    obj.filled = True
    obj.fill_color = 'pink'
    return obj


def make_body(x, y):
    obj = GOval(300, 300, x=x, y=y)
    obj.color = 'pink'
    obj.filled = True
    obj.fill_color = 'pink'
    return obj


if __name__ == '__main__':
    main()
