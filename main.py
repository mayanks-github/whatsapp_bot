import eel
import wx
import os
import whatsapp

eel.init('web')


@eel.expose
def generate_qr():
    print("hello Raya.")
    whatsapp.bot()


@eel.expose
def pythonFunction(wildcard="*"):
    app = wx.App(None)
    style = wx.FD_SAVE
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
        print(path)
    else:
        path = None
    dialog.Destroy()
    try:
        with open(path, 'r') as file:
            pass
    except IOError:
        wx.LogError("Cannot open file '%s'." % newfile)


eel.start('index.html', size=(1010, 700))
