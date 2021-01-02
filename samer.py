import os
import cv2

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

def check(folder):
    images = source(folder)
    count_images = len(images)
    to_remove = []

    print("Images: %d" % count_images)
    for i in range(count_images):
        print(images[i])
    for i in range(count_images):
        original = cv2.imread(images[i])
        print("Original: %s" % images[i])
        for j in range(count_images):
            if (j != i):
                compare = cv2.imread(images[j])
                print("Compare: %s" % images[j])
                if (original.shape == compare.shape):
                    print("\nThe images have the same size and channels")
                    difference = cv2.subtract(original, compare)
                    b, g, r = cv2.split(difference)

                    if (cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r)):
                        print("\nThe images are the same")
                        to_remove.append(compare)
        remove(to_remove)

def main():
    folder = input("Folder: ")
    check(folder)

if (__name__ == "__main__"):
    main()