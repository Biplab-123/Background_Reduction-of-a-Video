# Image-Processing
Background Reduction of a Video


prerequisite: 
1.Python IDLE 
2.required Libaries(Numpy,CV2)

import the video or i can say read the video
use reateBackgroundSubtractorMOG2 to subtract background
this basically a Algorithm Name as : MOG

use while(1): as if while true then only ret will work otherwise not
read the video by : ret, frame = cap.read()

apply the  MOG algorithm
fgmask = fgbg.apply(frame) 

show to use twice to see both the video

to break the loop use or press "s" key on keyboard
cv2.waitKey(1) & 0xFF == ord('f')

after that destroy all window






