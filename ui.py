import wx, ffmpy

def convert(inputPath,outputPath,enCode):
    convert = ffmpy.FFmpeg(
                inputs={inputPath : None},
                outputs={outputPath: enCode}
            )
    convert.run()
    return 

class homeFrame(wx.Frame):
    def __init__(self):
        super().__init__(None,title="转码")
        self.inputPath = ""
        self.outputPath = ""
        # self.inputPath = '/Users/uriah/Documents/Project/video covert/output111.mp4'
        # self.outputPath = self.inputPath[:-4] + '_output.webm'
        


        self.st_inputpath = wx.StaticText(self, label='源视频')
        self.tc_inputpath = wx.TextCtrl(self, pos=(80, 0), size=(300,-1))
        self.st_width = wx.StaticText(self, label='长',pos=(0,30))
        self.tc_width = wx.TextCtrl(self, pos=(80, 30), size=(50,-1))
        self.btn1 = wx.Button(self,label="转换成webm",pos=(0,90))
        self.btn2 = wx.Button(self,label="压缩mp4",pos=(0,120))
        self.btn3 = wx.Button(self,label="移除音频",pos=(0,150))
        self.Bind(wx.EVT_BUTTON,self._convert_webm,self.btn1)
        self.Bind(wx.EVT_BUTTON,self._convert_mp4,self.btn2)
        self.Bind(wx.EVT_BUTTON,self._remove_audio,self.btn3)
        self.st_note = wx.StaticText(self, label='使用说明:在输入框中粘贴文件的完整路径，\n然后点击"转换成webm"即可转码\n转换MP4需要输入宽度',pos=(0,180))

    def _remove_audio(self,e):
        inputPath = self.tc_inputpath.GetValue()
        outputPath = inputPath[:-4] + '_an.mp4'
        convert = ffmpy.FFmpeg(
                inputs={inputPath : None},
                outputs={outputPath: "-c:v copy -an"}
            )
        convert.run()
        self.st_note.SetLabel("音频移除成功")
        return

    def _convert_webm(self,e):
        inputPath = self.tc_inputpath.GetValue()
        outputPath = inputPath[:-4] + '_output.webm'
        convert = ffmpy.FFmpeg(
                inputs={inputPath : None},
                outputs={outputPath: "-y -c:v libvpx-vp9 -crf 28 -b:v 0 -b:a 128k -c:a libopus"}
            )
        convert.run()
        self.st_note.SetLabel("webm 转换成功")
        return


        

    def _convert_mp4(self,e):
        # scale = self.tc_width.GetValue()
        # if scale is not None:
        #     code = '-c:v libx264 -crf 28 -b:v 0 -vf scale='+scale+':-1'
        # else:
        #     code = '-c:v libx264 -crf 28 -b:v 0'
        inputPath = self.tc_inputpath.GetValue()
        outputPath = inputPath[:-4] + '_composer.mp4'
        convert = ffmpy.FFmpeg(
                inputs={inputPath : None},
                outputs={outputPath: '-y -c:v libx264 -crf 28 -b:v 0 '}
            )
        convert.run()
        self.st_note.SetLabel("转换成功")
        return 

app = wx.App()
homeFrame().Show()
app.MainLoop()