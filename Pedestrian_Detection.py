import cv2
video = cv2.VideoCapture('C:\\Users\\z014413\\Desktop\\Ramesh\\Project\\Car_Pedestrian_tracking\\Pedestrian.mp4')
pedestrian_track_file = 'haarcascade_fullbody.xml'
pedestrian_tracker = cv2.CascadeClassifier(pedestrian_track_file)
while True:
    (read_success,frame)=video.read()
    if read_success:
        gray_scale_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    else:
        break
    pedestrian = pedestrian_tracker.detectMultiScale(gray_scale_frame)
        # Draw rectangle in the image
    for (x, y, w, h) in pedestrian:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
            # Display Output
    cv2.imshow('Car Detected', frame)

        # To Close rather than autoclose by pressing enter key
    cv2.waitKey(-1)

    cv2.destroyAllWindows()
    print('Successfully Pedestrian detected')