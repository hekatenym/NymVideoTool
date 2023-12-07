import ffmpy
import os

#路径需要包含/
input_path = '' 
output_path = ''
if os.path.exists(output_path) == False:
    os.mkdir(output_path)

for root, dirs, files in os.walk(input_path):
    for f in files:
        extension_name = os.path.splitext(f)
        if extension_name[1] == '.mp4':
            output_videopath = output_path + "/" + os.path.basename(os.path.dirname(os.path.join(root,f)))
            print(output_videopath)
            if os.path.exists(output_videopath) == False:
                os.mkdir(output_videopath)
            convert_webm = ffmpy.FFmpeg(
                inputs={os.path.join(root,f): None},
                outputs={output_videopath + "/" + extension_name[0] + ".webm": '-y -c:v libvpx-vp9 -crf 28 -b:v 0 -an'}
                #-c:v 视频编码器  -vf 分辨率 -crf 清晰度 -b:v 比特率 -an 静音
            )
            convert_webm.run()
            convert_mp4 = ffmpy.FFmpeg(
                inputs={os.path.join(root,f): None},
                outputs={output_videopath + "/" + extension_name[0] + ".mp4": '-y -c:v libx264 -crf 24 -b:v 0 -an'}
            )
            convert_mp4.run()
