
import cv2


# Callback function
def draw_rectangle(event, x, y, flags, param):
    global pt1, pt2, top_left_clicked, bot_right_clicked

    if event is cv2.EVENT_LBUTTONDOWN:

        # Rest the rectangle (it checks if the rect there)
        if top_left_clicked is True and bot_right_clicked is True:
            pt1 = (0, 0)
            pt2 = (0, 0)

            top_left_clicked = False
            bot_right_clicked = False

        if top_left_clicked is False:
            pt1 = (x, y)
            top_left_clicked = True

        elif bot_right_clicked is False:
            pt2 = (x, y)
            bot_right_clicked = True


# global variables
pt1 = (0, 0)
pt2 = (0, 0)

top_left_clicked = False
bot_right_clicked = False

# connect protocol

cap = cv2.VideoCapture(0)

cv2.namedWindow('Test')
cv2.setMouseCallback('Test', draw_rectangle)

while True:

    ret, frame = cap.read()

    # drawing on the frame
    if top_left_clicked:
        cv2.circle(frame, center=pt1, radius=5, color=(0, 0, 255), thickness=-1)

    if top_left_clicked and bot_right_clicked:
        cv2.rectangle(frame, pt1, pt2, (0, 0, 255), 3)

    cv2.imshow('Test', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
