import cv2

#our input path
video = cv2.VideoCapture('C:\\Users\\z014413\\Desktop\\Ramesh\\Project\\Car_Pedestrian_tracking\\Tesla Autopilot Dashcam Compilation 2018 Version.mp4')

#Pretrained model
classifier_file = 'cars.xml'

#Car Classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

while True:
    (read_success,frame)=video.read()
    if read_success:
        gray_scale_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    else:
        break
        # detect cars
    cars = car_tracker.detectMultiScale(gray_scale_frame)
    # Draw rectangle in the image
    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # Display Output
    cv2.imshow('Car Detected', frame)

        # To Close rather than autoclose by pressing enter key
    cv2.waitKey()

    cv2.destroyAllWindows()
    print("successfully executed")
''' 
#img_file='C:\\Users\\z014413\\Desktop\\Ramesh\\Project\\Car_Pedestrian_tracking\\bmw10_ims\\1\\150079887.jpg'   
#create opencv img
img = cv2.imread(img_file)

#Pretrained model
classifier_file = 'cars.xml'


#Convert to gray scale image
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Car Classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

#detect cars
cars = car_tracker.detectMultiScale(gray_img)

#Draw rectangle in the image
for (x,y,w,h) in cars:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
print(cars)

#Display Output
cv2.imshow('Car Detected',img)

#To Close rather than autoclose by pressing enter key
cv2.waitKey()

cv2.destroyAllWindows()
print("successfully executed")'''