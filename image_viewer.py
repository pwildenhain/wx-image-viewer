import wx


class ImagePanel(wx.Panel):
    def __init__(self, parent, image_size):
        super().__init__(parent)

        img = wx.Image(*image_size)
        self.image_ctrl = wx.StaticBitmap(self, bitmap=wx.Bitmap(img))

        browse_btn = wx.Button(self, label="Browse")
        browse_btn.Bind(wx.EVT_BUTTON, self.on_browse)

        self.photo_text = wx.TextCtrl(self, size=(200, -1))

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)

        hsizer.Add(browse_btn, 0, wx.ALL, 5)
        hsizer.Add(self.photo_text)

        main_sizer.Add(self.image_ctrl, 0, wx.ALL, 5)
        main_sizer.Add(hsizer, 0, wx.ALL, 5)

        self.SetSizer(main_sizer)
        main_sizer.Fit(parent)
        main_sizer.Layout()

    def on_browse(self, event: wx.Event):
        """Browse for an image file
        Args:
            event: The event object
        """
        wildcard = "JPEG files (*.jpg)|*.jpg"

        with wx.FileDialog(
            None, "Choose a file", wildcard=wildcard, style=wx.ID_OPEN
        ) as dialog:
            if dialog.ShowModal() == wx.ID_OK:
                self.photo_text.SetValue(dialog.GetPath())


class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Image Viewer")

        panel = ImagePanel(self, image_size=(240, 240))
        self.Show()


if __name__ == "__main__":
    app = wx.App(redirect=False)
    frame = MainFrame()
    app.MainLoop()
