
import cv2


def ask_for_tracker():
    print("Welcome! What tracker API would you like to use ?")
    print("Enter 0 for BOOSTING: ")
    print("Enter 1 for MIL: ")
    print("Enter 2 for KCF: ")
    print("Enter 3 for TLD: ")
    print("Enter 4 for MEDIANFLOW: ")

    choice = input("Please select your tracker: ")

    if choice is '0':
        tracker = cv2.TrackerBoosting_create()
    if choice is '1':
        tracker = cv2.TrackerMIL_create()
    if choice is '2':
        tracker = cv2.TrackerKCF_create()
    if choice is '3':
        tracker = cv2.TrackerTLD_create()
    if choice is '4':
        tracker = cv2.TrackerMedianFlow_create()

    return tracker


tracker = ask_for_tracker()
tracker_name = str(tracker).split()[0][1:]

# Read video
cap = cv2.VideoCapture(0)

# Read first frame.
ret, frame = cap.read()

# Special function allows us to draw on the very first frame our desired ROI
roi = cv2.selectROI(frame, False)

# Initialize tracker with first frame and bounding box
ret2 = tracker.init(frame, roi)


while True:
    # Read a new frame
    ret3, frame = cap.read()

    # Update tracker
    success, roi = tracker.update(frame)

    # roi variable is a tuple of 4 floats
    # we need each value and we need them as integers
    (x, y, w, h) = tuple(map(int, roi))

    # Draw rectangle as Tracker moves
    if success:
        # Tracking success
        p1 = (x, y)
        p2 = (x + w, y + h)
        cv2.rectangle(frame, p1, p2, (0, 255, 0), 3)
    else:
        # Tracking failure
        cv2.putText(frame, "Failure to Detect Tracking!!", (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    # Display tracker type on frame
    cv2.putText(frame, tracker_name, (20, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    # Display result
    cv2.imshow(tracker_name, frame)

    # Exit if ESC pressed
    k = cv2.waitKey(1) & 0xFF

    if k is 27:
        break

cap.release()
cv2.destroyAllWindows()
