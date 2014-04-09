from photo import photo_small

from PIL import Image
def main():

    path = "/Users/Daniel/Pictures"
    print '111'
    img = Image.open(path+"/3.jpg")
    print '222'
    img_small = photo_small(img,25)
    print '333'
    print img.info
    print img.size
    print img_small.size
    print img_small.info

    img_small.save(path+"/111.jpg")


if __name__ == '__main__':
    main()

