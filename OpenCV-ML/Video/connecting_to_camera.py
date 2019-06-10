
import cv2


cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Windows -- *'DIVX'
# Linux -- *'XVID'

writer = cv2.VideoWriter('my_video.mp4', cv2.VideoWriter_fourcc(*'XVID'), 20, (width, height))

while True:

    ret, frame = cap.read()

    writer.write(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
writer.release()
cv2.destroyAllWindows()
