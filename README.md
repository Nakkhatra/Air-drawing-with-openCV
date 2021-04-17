# Air-drawing-with-openCV

This is done by tracking a specific colored object (Which is not present in the background) and adding trail points to the bounding box after finding the contour. 
You can write anything by moving the object infront of the camera.
The limiation is, this program tracks object by color, so if the same color as the object to track is present in the background too, then there are chances that 
the background might also be tracked and leave trail dots on camera.

But you can learn the basics of openCV if you run this code, such as getting contours, bounding boxes, creating trackbars which are tunable real time for masking 
specific colors (Which is done using bitwise_and operation), the basics of video capturing and working on each frame.
