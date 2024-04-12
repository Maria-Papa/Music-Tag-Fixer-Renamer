from asyncore import close_all
import tkinter as tk
from cli import start
from variables import black, green
from tkinter import BooleanVar, Scrollbar, StringVar, ttk, DISABLED, END, NORMAL, VERTICAL, NSEW, NS, EW, E

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Music Track Fixer")
        self.resizable(False, False)
        self._center_window()
        self._create_grid("20 20 20 20")
        self._create_widgets()

    def _center_window(self, per_of_screen_w=40, per_of_screen_h=60):
        # Get the screen dimension
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()

        # Covert the percentage of the screen to window width & height
        ww = int(sw*(per_of_screen_w/100))
        wh = int(sh*(per_of_screen_h/100))

        # Find the center point
        center_x = int(sw/2 - ww / 2)
        center_y = int(sh/2 - wh / 2)

        # Set the position of the window to the center of the screen
        self.geometry(f'{ww}x{wh}+{center_x}+{center_y}')

    def _create_grid(self, padding):
        self.main_frame = ttk.Frame(self, padding=padding)
        self.main_frame.pack(fill="both", expand=True)
        self._configure_grid()
    
    def _configure_grid(self):
        self.main_frame.columnconfigure(1, weight=1)
        # self.main_frame.columnconfigure(3, weight=4)
        self.main_frame.rowconfigure(1, weight=2)
        
    def _start_get_meta(self):
        start(self, "get_meta")
        
    def _start_fix_meta(self):
        start(self, "fix_meta")

    def _start_rename(self):
        start(self, "rename")

    def _create_widgets(self):
        # ROW 0 - PATH LABEL
        self.path_label = ttk.Label(self.main_frame, text="Music Files Location:")
        self.path_label.grid(row=0, column=0)

        # ROW 0 - PATH ENTRY
        self.path       = StringVar()
        self.path_entry = ttk.Entry(self.main_frame, width=150, textvariable=self.path)
        self.path_entry.grid(row=0, column=1, sticky=EW, padx=20)

        # ROW 0 - SUBDIR CHECKBUTTON
        self.subdir              = BooleanVar()
        self.sub_dir_ckeckbutton = ttk.Checkbutton(self.main_frame, text="Include Subdirectories", name="sub_dir", variable=self.subdir, onvalue=1, offvalue=0, state=NORMAL)
        self.sub_dir_ckeckbutton.grid(row=0, column=2, sticky=E)

        # ROW 1 - OUTPUT TEXT
        self.output      = StringVar()
        self.output_text = tk.Text(self.main_frame, state=DISABLED)
        self.output_text.grid(row=1, column=0, columnspan=4, sticky=NSEW, pady=20)

        # ROW 1 - SCROLLBAR
        self.scroll = Scrollbar(self.main_frame, orient=VERTICAL, command=self.output_text.yview)
        self.scroll.grid(row=1, column=0, columnspan=4, sticky=(NS, E), pady=20)

        # BUTTONS STYLE
        style = ttk.Style()
        style.configure("TButton", font=("calibri", 16, "bold"), background=green, foreground=green)

        # ROW 2 - BUTTON GET META
        self.get_meta_button = ttk.Button(self.main_frame, text="Get Metadata", command=self._start_get_meta)
        self.get_meta_button.grid(row=2, column=0, columnspan=3, sticky=EW)

        # ROW 3 - BUTTON FIX META
        self.fix_meta_button = ttk.Button(self.main_frame, text="Fix Metadata", command=self._start_fix_meta)
        self.fix_meta_button.grid(row=3, column=0, columnspan=3, sticky=EW, pady=20)

        # ROW 4 - BUTTON RENAME
        self.rename_button = ttk.Button(self.main_frame, text="Rename", command=self._start_rename)
        self.rename_button.grid(row=4, column=0, columnspan=3, sticky=EW)

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
