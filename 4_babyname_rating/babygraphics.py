"""
File: babygraphics.py
Name: QiaosiPan
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    return GRAPH_MARGIN_SIZE+(width-2*GRAPH_MARGIN_SIZE)//len(YEARS)*year_index     # // for int


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    # draw the fixed horizontal line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
    # draw the fixed vertical line
    for year_index in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, year_index)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)
        canvas.create_text(x, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=str(YEARS[year_index]), anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    num = -1
    for name in lookup_names:
        # variable setting
        x = []
        y = []
        name_tag = []
        color = COLORS[num % len(COLORS)]
        # if num < 4:
        #     num += 1
        #     color = COLORS[num]
        # else:
        #     color = 'blue'
        # get coordinates and text of each data points, then store as x(list), y(list), name_tag(list)
        for year in YEARS:
            x.append(get_x_coordinate(CANVAS_WIDTH, YEARS.index(int(year))))
            if str(year) in name_data[name]:
                # if rank is under 1000, count y and name_tag with rank
                rank = name_data[name][str(year)]
                y.append(GRAPH_MARGIN_SIZE + (CANVAS_HEIGHT-2*GRAPH_MARGIN_SIZE) / 1000 * int(rank))
                name_tag.append(' '+name + ' ' + rank)
            else:
                # if rank is out of 1000, y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                y.append(CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
                name_tag.append(' '+name+' *')

        # draw data line (with two method)

        # method1 : Recursion #
        draw_data(canvas, len(YEARS)-1, x, y, name_tag, color)

        # method2 : For loop #
        # for i in range(len(YEARS)):
        #     if i == 0:
        #         canvas.create_text(x[i], y[i], text=name_tag[i], fill=color, anchor=tkinter.SW)
        #     else:
        #         canvas.create_text(x[i], y[i], text=name_tag[i], fill=color, anchor=tkinter.SW)
        #         canvas.create_line(x[i], y[i], x[i-1], y[i-1], fill=color)


# function for Recursion
def draw_data(canvas, years, x, y, name_tag, color):
    if years == 0:
        canvas.create_text(x[years], y[years], text=name_tag[years], fill=color, anchor=tkinter.SW)
    else:
        draw_data(canvas, years-1, x, y, name_tag, color)
        canvas.create_text(x[years], y[years], text=name_tag[years], fill=color, anchor=tkinter.SW)
        canvas.create_line(x[years], y[years], x[years-1], y[years-1], fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
