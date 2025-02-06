from simpletk import *
from tkinter import RIGHT, filedialog


class TImageViewer(TApplication):
    def __init__(self):
        TApplication.__init__(self, "image viewer")
        self.position = (600, 300)
        self.size = (720, 480)
        self.background = "#5544BB"
        self.upPanel = TPanel(self,
                     relief="raised",
                     height=65,
                     bd=6)
        self.upPanel.align = "top"
        self.upPanel.background = "#01aaAB"
        self.opButton = TButton(self.upPanel,
                       width=110,
                       height=40,
                       text="Open file")
        self.opButton.position = (5, 5)
        self.opButton.background = "#3377DF"
        self.opButton.font = 30
        self.flag = TCheckBox(self.upPanel,
                              text="В центре")
        self.flag.position = (215, 5)
        self.flag.background = "#01aaAB"
        self.flag.font = 30
        self.flag2 = TCheckBox(self.upPanel,
                               text="В центре")
        self.flag2.position = (300, 5)
        self.flag2.background = "#01aaAB"
        self.flag2.font = 30
        self.img = TImage(self,
                          bg="#0177aa")
        self.img.align = "client"
        self.img2 = TImage(self,
                           bg="#0177aa")
        self.img2.align = "client"

        self.opButton.onClick = self.selectFile
        self.flag.onChange = self.fCenter
        self.flag2.onChange = self.fCenter2

    def selectFile(self, sender):
        fname = filedialog.askopenfilenames(filetypes=[("Все файлы", "*.*"), ("Файлы GIF", "*.gif")])
        if len(fname) == 1:
           self.img.picture = fname[0]
        elif len(fname) == 2:
            self.img.picture = fname[0]
            self.img2.picture = fname[1]

    def fCenter(self, sender):
        if self.flag.checked:
            self.img.center = 1
        else:
            self.img.center = 0

    def fCenter2(self, sender):
        if self.flag2.checked:
            self.img2.center = 1
        else:
            self.img2.center = 0






