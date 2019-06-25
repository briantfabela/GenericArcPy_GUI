# python 2.7.13 ArcGIS Distribution

from Tkinter import *
from os import *
import tkFileDialog
import arcpy

logo_path = r'mxd_icon.ico'

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def load_file(self):
        self.mxd_filepath = tkFileDialog.askopenfilename(initialdir=getcwd(),
                                                         filetypes=[("Map Files", "*.mxd")])
        self.file_path.config(state='normal') # 'enable' widget to update text
        self.file_path.delete(0, 'end')
        self.file_path.insert(0, self.mxd_filepath) # update text
        self.file_path.config(state='disabled') # 'disable' widget so that user cannot edit

        self.save_to["state"] = "normal"

    def save_path(self):
        self.outfolder = tkFileDialog.askdirectory()

        self.save_file_path.config(state='normal')
        self.save_file_path.delete(0, 'end')
        self.save_file_path.insert(0, self.outfolder)
        self.save_file_path.config(state='disabled')

        self.run_process_btn["state"] = "normal"

    def run_process(self):
        print('Beep Boop!')

    def createWidgets(self):

            # 1ST ROW WIDGETS
        
        # window top bar properties
        self.winfo_toplevel().title("Layer Table of Contents to File Geodatabase Converter")
        
        # Label "Selected File Path: "
        self.fs_label = Label(self)
        self.fs_label["text"] = "Select .mxd File: "
        self.fs_label.grid(row=0, column=0, padx =(10, 0), pady=(15,5))

        # Entry field containing selected path
        self.file_path = Entry(self, width=80, state='disabled')
        self.file_path.grid(row=0, column=1, padx=(0, 10), pady=(15,5)) # pad 10 px

        # Select file to load
        self.file_select = Button(self, command=self.load_file)
        self.file_select["text"] = "Select File"
        self.file_select.grid(row=0, column=2, pady=(15,5), sticky= 'W')

            # 2ND ROW WIDGETS
        
        # Label "Save To: "
        self.save_loc = Label(self)
        self.save_loc['text'] = "Save To: "
        self.save_loc.grid(row=1, column=0, padx=(10,0), sticky="E")

        # Entry Field containing selected 'save to' path
        self.save_file_path = Entry(self, width=80, state='disabled')
        self.save_file_path.grid(row=1, column=1, padx=(0, 10))

        # Select 'Save Path' Button
        self.save_to = Button(self, state='disabled', command=self.save_path)
        self.save_to['text'] = 'Select GDB'
        self.save_to.grid(row=1, column=2, padx=(0, 10), sticky= 'W')

            # 3RD TOW WIDGETS

        # Explaination
        self.helpinfo = Label(self)
        self.helpinfo['text'] = "Your selected mxd's table of contents will be Copied into the selected File Geodatabase"
        self.helpinfo.grid(row=2, column=1, padx=(2,2), pady=(5,15), sticky='W')

        # Run Process Button
        self.run_process_btn = Button(self, state='disabled', command = self.run_process)
        self.run_process_btn["text"] = "Run"
        self.run_process_btn.grid(row=2, column=2, pady=(5,15), sticky= 'W')

if __name__ == '__main__':
    root = Tk()
    root.wm_iconbitmap(logo_path)
    Application(master=root).mainloop()


