#Jorge Hurtado Edited Version
#Removed video import, used cv2 capture video function, applied b&w filter to the edge image created 

from __future__ import print_function

import cv2 as cv
import numpy as np




# built-in module
import sys


def main():
    try:
        fn = sys.argv[1]
    except:
        fn = 0

    def nothing(*arg):
        pass

    cv.namedWindow('edge')
    cv.createTrackbar('thrs1', 'edge', 2000, 5000, nothing)
    cv.createTrackbar('thrs2', 'edge', 4000, 5000, nothing)

    cap = cv.VideoCapture(0)
    while True:
        flag, img = cap.read()
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        thrs1 = cv.getTrackbarPos('thrs1', 'edge')
        thrs2 = cv.getTrackbarPos('thrs2', 'edge')
        edge = cv.Canny(gray, thrs1, thrs2, apertureSize=5)
        vis = img.copy()
        vis = np.uint8(vis/2.)
        vis[edge != 0] = (0, 255, 0)
        cv.imshow('edge', cv.cvtColor(vis, cv.COLOR_BGR2GRAY))
        ch = cv.waitKey(5)
        if ch == 27:
            break

    print('Done')


if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()
