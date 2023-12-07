import ffmpy
import os

inputPath = '/Users/uriah/Documents/Project/video covert/output111.mp4'
outPutPath_mp4 = inputPath[:-4] + '_output.mp4'
outPutPath_webm = inputPath[:-4] + '_output.webm'
convertWebm = ffmpy.FFmpeg(
                inputs={inputPath : None},
                outputs={outPutPath_webm: '-c:v libvpx-vp9 -crf 18 -b:v 0 -b:a 128k -c:a libopus'}
                # outputs={'/Users/uriah/Documents/Project/GD612/' + extension_name[0] + '/' + extension_name[0]+'.mp4': '-c:v libx264 -crf 30 -b:v 0 -b:a 128k '}
            )
# def convertWebm(inputPath,outputPath,enCode):
#     convert = ffmpy.FFmpeg(
#                 inputs={inputPath : None},
#                 outputs={outputPath: enCode}
#             )
#     convert.run()
#     return

# convertWebm(inputPath,outPutPath_webm,'-c:v libx264 -crf 30 -b:v 0 -b:a 128k')


# convertMp4 = ffmpy.FFmpeg(
#                 inputs={inputPath : None},
#                 # outputs={outPutPath_mp4: '-c:v libvpx-vp9 -crf 30 -b:v 0 -b:a 128k -c:a libopus'}
#                 outputs={outPutPath_mp4: '-c:v libx264 -crf 30 -b:v 0 -b:a 128k '}
#             )
# convertMp4.run()
convertWebm.


# stream = ffmpeg.input(os.path.join(root,f))
            # stream = ffmpeg.output(stream,'/Users/uriah/Documents/DocumentExchange/170_webm/' + extension_name[0] + '/' + extension_name[0]+'.webm',vcodec="libvpx-vp9",format="webm",crf="30")

# stream = ffmpeg.input("/Users/uriah/GT_FileRecv/转序列帧 转webm格式/01_首屏/WM170_开屏_1080P_0129_1.mp4")
# stream = ffmpeg.output(stream,'/Users/uriah/Documents/DocumentExchange/170_webm/output.webm',vcodec="libvpx-vp9",format="webm",crf="30")

