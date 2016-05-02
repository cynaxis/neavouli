from __future__ import unicode_literals

# easy_thumbnails face cropping processor
# Much of the below taken from http://stackoverflow.com/a/13243712/669631

import cv2
import numpy

# Select one of the haarcascade files:
#   haarcascade_frontalface_alt.xml  <-- Best one?
#   haarcascade_frontalface_alt2.xml
#   haarcascade_frontalface_alt_tree.xml
#   haarcascade_frontalface_default.xml
#   haarcascade_profileface.xml
face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')


def detect_faces(im):
    # This function takes a PIL image and finds the patterns defined in the
    # haarcascade function modified from: http://www.lucaamore.com/?p=638

    # Convert a PIL image to a greyscale cv image
    cv_im = cv2.cvtColor(numpy.array(im), cv2.COLOR_RGB2GRAY)
    # Equalize the histogram
    cv_im = cv2.equalizeHist(cv_im)

    # Detect the faces
    faces = face_cascade.detectMultiScale(
        cv_im,
        scaleFactor=1.1, minNeighbors=3, minSize=(20, 20)
        )
    return faces

def face_crop_bounds(im):
    source_x, source_y = [int(v) for v in im.size]
    faces = detect_faces(im).tolist()
    if not faces:
        return None
    cropBox = [0, 0, 0, 0]
    for face in faces:
        if face[2] > cropBox[2] or face[3] > cropBox[3]:
            cropBox = face

    xDelta = int(max(cropBox[2] * 0.4, 0))
    yDelta = int(max(cropBox[3] * 0.4, 0))

    # Convert cv box to PIL box [left, upper, right, lower]
    if cropBox == [0, 0, 0, 0]:
        return None

    return [
            max(cropBox[0] - xDelta, 0),
            max(cropBox[1] - yDelta, 0),
            min(cropBox[0] + cropBox[2] + xDelta, source_x - 1),
            min(cropBox[1] + cropBox[3] + yDelta, source_y - 1)
    ]
