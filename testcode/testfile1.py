#!/usr/bin/env python
# -*- coding: utf-8 -*-

#-Imports.----------------------------------------------------------------------
#--Python Imports.
import sys

#--wxPython Imports.
import wx

class MyNamePanel(wx.Panel):
    def __init__(self, parent, id=wx.ID_ANY,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.BORDER_SUNKEN, name='panel'):
        wx.Panel.__init__(self, parent, id, pos, size, style, name)

class MyNameFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString,
                 pos=wx.DefaultPosition, size=wx.DefaultSize,
                 style=wx.DEFAULT_FRAME_STYLE, name='frame'):
        wx.Frame.__init__(self, parent, id, title, pos, size, style, name)
        global gMainWin
        gMainWin = self
        panel = MyNamePanel(self)
        self.Bind(wx.EVT_CLOSE, self.OnDestroy)

    def OnDestroy(self, event):
        self.Destroy()

class MyNameApp(wx.App):
    def OnInit(self):
        self.SetClassName('MyNameApp')
        self.SetAppName('MyNameApp')
        gMainWin = MyNameFrame(None)
        gMainWin.SetTitle('MyNameFrame')
        self.SetTopWindow(gMainWin)
        gMainWin.Show()
        return True

if __name__ == '__main__':
    gApp = MyNameApp(redirect=False,
            filename=None,
            useBestVisual=False,
            clearSigInt=True)

    gApp.MainLoop()
