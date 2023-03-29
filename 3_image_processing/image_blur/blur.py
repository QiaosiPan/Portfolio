"""
File: blur.py
Name: QiaosiPan
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    ## initial setting
    x_pixel = img.width     # get the old_img size
    y_pixel = img.height    # get the old_img size
    img_new = SimpleImage.blank(x_pixel,y_pixel)    # create img_new with old_img's size
    ## start scaning
    ## i,j to define current pixel
    for i in range(x_pixel):
        for j in range(y_pixel):
            rgb_sum = (0,0,0)
            count_neighbor = 0
            ## del_x,del_y to define 3*3 filter
            for del_x in range(-1,2,1):
                for del_y in range(-1,2,1):
                    x_n = i + del_x
                    y_n = j + del_y
                    ## if the neighbor pixels are inside img_new's boundary, get their rgb values and sum
                    if ((x_n >= 0) and (x_n < x_pixel) and (y_n >= 0) and (y_n < y_pixel)) :
                        count_neighbor += 1
                        rgb_neighbor = img.get_pix(x_n,y_n)
                        rgb_sum = (rgb_sum[0]+rgb_neighbor[0],rgb_sum[1]+rgb_neighbor[1],rgb_sum[2]+rgb_neighbor[2])
            ## count average rgb value and return img_new
            blur_r = int(rgb_sum[0]/count_neighbor)
            blur_g = int(rgb_sum[1]/count_neighbor)
            blur_b = int(rgb_sum[2]/count_neighbor)
            img_new.set_pix(i,j,(blur_r,blur_g,blur_b))
    return img_new
    pass


def main():
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
