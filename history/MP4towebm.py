import ffmpy
import os
# args = {
#     "video_bitrate" : "0",
#     "audio_bitrate" : "128k",
#     "acodec" : "libopus",
#     "vcodec" : "libvpx-vp9",
#     "video_bitrate" : "1M",
#     "format" : "webm",
#     "crf" : "30"
# }

for root, dirs, files in os.walk(''):
    for f in files:
        extension_name = os.path.splitext(f)
        if extension_name[1] == '.mp4':
            os.mkdir('' + extension_name[0])
            # print(os.path.join(root,f))
            ff = ffmpy.FFmpeg(
                inputs={os.path.join(root,f): None},
                outputs={'' + extension_name[0] + '/' + extension_name[0]+'.webm': '-c:v libvpx-vp9 -crf 30 -b:v 0 -b:a 128k -c:a libopus'}
                # outputs={'' + extension_name[0] + '/' + extension_name[0]+'.mp4': '-c:v libx264 -crf 30 -b:v 0 -b:a 128k '}
            )
            ff.run()



# stream = ffmpeg.input(os.path.join(root,f))
# stream = ffmpeg.output(stream,'' + extension_name[0] + '/' + extension_name[0]+'.webm',vcodec="libvpx-vp9",format="webm",crf="30")

# stream = ffmpeg.input("")
# stream = ffmpeg.output(stream,'',vcodec="libvpx-vp9",format="webm",crf="30")

