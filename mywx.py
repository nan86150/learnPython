import wx #1
import os

class App(wx.App):#2

    def OnInit(self): #3
        frame = wx.Frame(parent=None, title='Bare')
        frame.Show()
        return True

app = App(0) #4
app.MainLoop() #5

# import sys, os
# from wxPython.wx import *
# class main_window(wxFrame):
	# def __init__(self, parent, id, title):
		# wxFrame.__init__(self, parent, -1, title, size = (200, 100),style=wxDEFAULT_FRAME_STYLE|wxNO_FULL_REPAINT_ON_RESIZE)
		# self.control = wxTextCtrl(self, -1, style=wxTE_MULTILINE)
		# self.Show(true)
	
# class App(wxApp):
	# def OnInit(self):
		# frame =main_window(None, -1, "wxPython: (A Demonstration)")
		# self.SetTopWindow(frame)
		# return true

# app = App(0)
# app.MainLoop()