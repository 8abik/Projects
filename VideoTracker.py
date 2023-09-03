import cv2

tracker = cv2.TrackerMIL_create()

cap = cv2.VideoCapture(0)

success, frame = cap.read()
bbox = cv2.selectROI("Tracking", frame, False)
tracker.init(frame, bbox)

def put_text(img, text, position):
    cv2.putText(img, text, position, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 255), 2)


while True:
    timer = cv2.getTickCount()
    success, img = cap.read()
    success, bbox = tracker.update(img)

    if success:
        x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
        cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 3, 3)
        put_text(img, "Tracking", (100, 75))
    else:
        put_text(img, "Lost", (100, 75))

    put_text(img, "Fps:", (20, 40))
    put_text(img, "Status:", (20, 75))

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    fps_color = (0, 255, 0) if fps > 60 else ((0, 0, 255) if fps < 20 else (255, 0, 0))
    put_text(img, str(int(fps)), (75, 40))

    cv2.imshow("Tracking", img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
