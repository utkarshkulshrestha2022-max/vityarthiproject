import cv2
import numpy as np

cap = cv2.VideoCapture("/Users/utkarshkulshrestha/Downloads/CSE-3010/vityarthiproject/video2.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize
    frame = cv2.resize(frame, (640, 360))

    # Preprocessing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edges = cv2.Canny(blur, 100, 200)

    # Region of interest (triangle mask)
    height, width = edges.shape
    mask = np.zeros_like(edges)
    pts = np.array([[(0,height),(width//2,height//2),(width,height)]])
    cv2.fillPoly(mask, pts, 255)
    roi = cv2.bitwise_and(edges, mask)

    # Hough Transform
    lines = cv2.HoughLinesP(roi, 1, np.pi/180, 50, maxLineGap=150)

    # Draw lanes
    if lines is not None:
        for x1,y1,x2,y2 in lines[:,0]:
            cv2.line(frame, (x1,y1),(x2,y2),(0,255,0), 3)

    cv2.imshow("Lane Segmentation", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("error")
    exit()

while True:
    ret, frame = cap.read()

    if not ret or frame is None:
        print("warning")
        continue
rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
pixels = rgb.reshape((-1,3))
pixels = np.float32(pixels)

k = 3
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
_, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

segmented = centers[labels.flatten()].reshape(rgb.shape)
seg_gray = cv2.cvtColor(segmented, cv2.COLOR_RGB2GRAY)

_, mask = cv2.threshold(seg_gray, 200, 255, cv2.THRESH_BINARY)
