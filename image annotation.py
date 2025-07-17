import cv2
import matplotlib.pyplot as plt

image_path="ant.jpg"
image=cv2.imread(image_path)
image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
h,w,c=image_rgb.shape

rect1_width=150
rect1_height=150

top_left1=(20,20)
botton_right1=(top_left1[0]+rect1_width, top_left1[1]+rect1_height)
cv2.rectangle(image_rgb,top_left1,botton_right1,(0,255,255),3)


rect2_width=200
rect2_height=150
top_left2=(w-rect2_width-20,h-rect2_height-20)
botton_right2=(top_left2[0]+rect2_width,top_left2+rect2_height)
cv2.rectangle(image_rgb,top_left2,botton_right2,(255,0,255),3)

center1_x=top_left1[0]+rect1_width//2
center1_y=top_left1[1]+rect1_height//2

cv2.circle(image_rgb,(center1_x,center1_y),15,(0,255,0),-1)


plt.imshow(image_rgb)
plt.title("Annotation of image")
plt.show()
