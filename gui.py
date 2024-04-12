import tkinter as tk
from cli import start
from variables import black
from tkinter import LEFT, NE, NW, SE, BooleanVar, Scrollbar, StringVar, ttk, DISABLED, END, NORMAL, VERTICAL, NS, N, W, E, S, EW

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Music Track Fixer")
        self.resizable(0, 0)
        self._center_window(1500, 800)

        self.main_frame = self._create_grid("25 25 25 25")
        
        # self._configure_grid()
        self._create_widgets()

    def _center_window(self, ww, wh):
        # Get the screen dimension
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()

        # Find the center point
        center_x = int(sw/2 - ww / 2)
        center_y = int(sh/2 - wh / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f'{ww}x{wh}+{center_x}+{center_y}')

    def _create_grid(self, padding):
        mf = ttk.Frame(self, padding=padding)
        mf.grid(column=0, row=0, sticky=(N, W, E, S))
        return mf
    
    def _configure_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=3)
        
    def _start(self):
        start(self)

    def _create_widgets(self):
        # PATH LABEL
        self.path_label = ttk.Label(self.main_frame, text="Music Files Location:")
        self.path_label.grid(row=0, column=0, sticky=NW, padx=5, pady=5)

        # PATH ENTRY
        self.path       = StringVar()
        self.path_entry = ttk.Entry(self.main_frame, width=100, textvariable=self.path)
        self.path_entry.grid(row=0, column=1, sticky=NW, padx=5, pady=5)

        # SUBDIR CHECKBUTTON
        self.subdir              = BooleanVar()
        self.sub_dir_ckeckbutton = ttk.Checkbutton(self.main_frame, text="Include Subdirectories", name="sub_dir", variable=self.subdir, onvalue=1, offvalue=0, state="normal")
        self.sub_dir_ckeckbutton.grid(row=0, column=2, sticky=NE, padx=5, pady=5)

        # OUTPUT TEXT
        self.output      = StringVar()
        self.output_text = tk.Text(self.main_frame, state=DISABLED)
        self.output_text.grid(row=1, column=0, columnspan=3, rowspan=3, sticky=EW, padx=5, pady=5)

        # SCROLLBAR
        self.scroll = Scrollbar(self.main_frame, orient=VERTICAL, command=self.output_text.yview)
        self.scroll.grid(row=1, column=0, columnspan=3, rowspan=3, sticky=(NS, E), padx=5, pady=5)

        # START BUTTON
        self.start_button = ttk.Button(self.main_frame, text="Start", command=self._start)
        self.start_button.grid(row=5, column=0, columnspan=3, rowspan=2, sticky=EW, padx=5, pady=5)

    def get_subdir_value(self):
        return self.subdir.get()
    
    def get_path_value(self):
        return self.path.get()
    
    def set_output_value(self, output_value, fg=black, delete=False):
        self.output_text.configure(state=NORMAL, fg=fg)

        if delete is True:
            self.output_text.delete("1.0", END)

        self.output_text.insert(END, output_value)
        self.output_text.configure(state=DISABLED)

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
