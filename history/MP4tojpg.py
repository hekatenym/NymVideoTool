from cv2 import cv2
import os
for root, dirs, files in os.walk(''):
    for f in files:
        try: 
            extension_name = os.path.splitext(f)
            if extension_name[1] == '.mp4':
                # os.mkdir('' + extension_name[0])
                # print(os.path.join(root,f))
                vc = cv2.VideoCapture(os.path.join(root,f))
                rval = vc.isOpened()
                c=0
                while rval:
                    rval, frame = vc.read()
                    cv2.imwrite(''+ extension_name[0] + '/' + str(c) + '.jpg', frame)
                    print(''+ extension_name[0] + '/' + str(c) + '.jpg')
                    c=c+1
                vc.release()
        except:
            continue