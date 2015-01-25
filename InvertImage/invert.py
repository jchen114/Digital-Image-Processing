__author__ = 'jacobchen2272'
import Image
import webbrowser
tmp_file_name = 'inverse_img.jpg'


def invert(im):
    im.load()
    source = im.split()
    r, g, b = 0, 1, 2
    r_img = source[r].point(lambda i: 255 - i)
    g_img = source[g].point(lambda i: 255 - i)
    b_img = source[b].point(lambda i: 255 - i)

    inv_img = Image.merge(im.mode, [r_img, g_img, b_img])
    inv_img.save(tmp_file_name)
    webbrowser.open(tmp_file_name)

    return

if __name__ == "__main__":
    im = Image.open('./LittlePeople.jpg')
    invert(im)