
import cv2


# mouse callback function
def draw_circle(event, x, y, flags, param):
    global center, clicked

    # get mouse click on down
    if event is cv2.EVENT_LBUTTONDOWN:
        center = (x, y)
        clicked = False

    if event is cv2.EVENT_LBUTTONUP:
        clicked = True


# Globals (Haven`t drawn anything yet!)
center = (0, 0)
clicked = False

# Capture Video
cap = cv2.VideoCapture(0)

# Create a named window
cv2.namedWindow('Test')

# Bind draw_circle function to mouse clicks
cv2.setMouseCallback('Test', draw_circle)


while True:

    ret, frame = cap.read()

    if clicked:
        cv2.circle(frame, center=center, radius=50, color=(255, 0, 0), thickness=5)

    cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF is ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
