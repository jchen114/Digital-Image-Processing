__author__ = 'jacobchen2272'
import Image, ImageEnhance
import webbrowser
img_loc = 'segmented_img.jpg'

threshold = 83
dist_x = 5
dist_y = 5
grayscale_factor = 15


def segment_coins(img):
    pix = img.load()
    (w, h) = img.size
    dist = []
    for y in range(0, h):
        if y % 2 == 0:
            # scan one way
            for x in range(0, w):
                segment(x, y, pix, dist)
        else:
            # scan the other way
            for x in range(w-1, -1, -1):
                segment(x, y, pix, dist)

    img.save(img_loc)
    webbrowser.open(img_loc)
    return


def segment(x, y, pix, dist):
    if pix[x, y] < threshold:
        pix[x, y] = 0
    else:
        reg_found = False
        # Check the distances for each region
        for reg in range(len(dist)):
            (a, b) = dist[reg]
            (x_dist, y_dist) = calculate_distance((a, b), (x, y))
            if y_dist < dist_y and x_dist < dist_x:
                # then this pixel belongs to that region
                pix[x, y] = 255 - grayscale_factor*reg
                # update the dist array for that latest pixel
                dist[reg] = (x, y)
                reg_found = True
                break
        if not reg_found: # Automatic separate region because they are separated vertically
            dist.append((x, y))
            pix[x, y] = 255 - grayscale_factor*len(dist)
    return


def calculate_distance((a, b), (c, d)):
    return (abs(c-a), abs(d-b))


if __name__ == "__main__":
    img = Image.open('./coins.png')
    segment_coins(img)