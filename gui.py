import tkinter as tk
import tkinter.font as font
from turtle import width
from cli import start
from variables import black, green
from tkinter import LEFT, NE, NSEW, NW, SE, BooleanVar, Grid, Scrollbar, StringVar, ttk, DISABLED, END, NORMAL, VERTICAL, NS, N, W, E, S, EW

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Music Track Fixer")
        self.resizable(False, False)
        self._center_window()
        self._create_grid("25 25 25 25")
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
        self._configure_grid()
        self.main_frame.pack(fill='both', expand=True)
    
    def _configure_grid(self):
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.columnconfigure(1, weight=1)
        self.main_frame.columnconfigure(2, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.rowconfigure(1, weight=3)
        self.main_frame.rowconfigure(2, weight=1)
        
    def _start(self):
        start(self)

    def _create_widgets(self):
        # PATH LABEL
        self.path_label = ttk.Label(self.main_frame, text="Music Files Location:")
        self.path_label.grid(row=0, column=0, sticky=W, padx=5, pady=5)

        # PATH ENTRY
        self.path       = StringVar()
        self.path_entry = ttk.Entry(self.main_frame, width=150, textvariable=self.path)
        self.path_entry.grid(row=0, column=1, sticky=EW, padx=5, pady=5)

        # SUBDIR CHECKBUTTON
        self.subdir              = BooleanVar()
        self.sub_dir_ckeckbutton = ttk.Checkbutton(self.main_frame, text="Include Subdirectories", name="sub_dir", variable=self.subdir, onvalue=1, offvalue=0, state="normal")
        self.sub_dir_ckeckbutton.grid(row=0, column=2, sticky=E, padx=5, pady=5)

        # OUTPUT TEXT
        self.output      = StringVar()
        self.output_text = tk.Text(self.main_frame, state=DISABLED)
        self.output_text.grid(row=1, column=0, columnspan=3, sticky=NSEW, padx=5, pady=5)

        # SCROLLBAR
        self.scroll = Scrollbar(self.main_frame, orient=VERTICAL, command=self.output_text.yview)
        self.scroll.grid(row=1, column=0, columnspan=3, sticky=(NS, E), padx=5, pady=5)

        # START BUTTON
        style = ttk.Style()
        style.configure("TButton", font=("calibri", 16, "bold"), background=green, foreground=green)
        self.start_button = ttk.Button(self.main_frame, text="Start", command=self._start)
        self.start_button.grid(row=2, column=0, columnspan=3, sticky=EW, padx=5, pady=5)


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
