import os
import cv2
import sys
import datetime

def source(folder):
    list = []
    images = os.listdir(folder)
    count = len(images)
    if (folder[len(folder) - 1] == '/'):
        spliter = ''
    else:
        spliter = '/'
    
    for i in range(count):
        if (os.path.isfile("%s%c%s" % (folder, spliter, images[i]))):
            list.append("%s%c%s" % (folder, spliter, images[i]))
    return (list)

def remove(list):
    count = len(list)

    for i in range(count):
        print("Removing: %s" % list[i])
        os.remove(list[i])

def colors(c, f):
    data = {
        "reset"  : "0",
        "red"    : "31",
        "green"  : "32",
        "yellow" : "33",
        "blue"   : "34",
        "purple" : "35",
        "cyan"   : "36",
        "white"  : "37"
    }
    if data.get("%s" % c) != None and (f >= 0 and f <= 5):
        return ("\033[%s;%sm" % (f, data.get("%s" % c)))
    return (None)

def check(folder):
    images = source(folder)
    count_images = len(images)
    to_remove = []

    percent = 0

    print("Starting...", end = '\n\n')

    for i in range(count_images):
        original = cv2.imread(images[i])
        print("Original: %s%s%s" % (
            colors("green", 1),
            images[i],
            colors("reset", 0)
        ))
        for j in range(i + 1, count_images):
            if (j != i):
                print("Compare: %s%s%s" % (
                    colors("purple", 1),
                    images[j],
                    colors("reset", 0)
                ))
                compare = cv2.imread(images[j])
                if (original.shape == compare.shape):
                    difference = cv2.subtract(original, compare)
                    b, g, r = cv2.split(difference)

                    if (cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r)):
                        print("n°%d n°%d are equals" % (i, j))
                        to_remove.append(images[j])
                        double += 1
            remove(to_remove)
    print("Finished")

def main():
    folder = sys.argv[1]
    check(folder)

if (__name__ == "__main__"):
    main()