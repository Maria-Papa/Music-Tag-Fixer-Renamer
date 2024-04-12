import tkinter as tk
from tkinter import BooleanVar, StringVar, ttk, DISABLED, END, NORMAL, NS, N, W, E, S
from test_funcs import start

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Music Track Fixer")
        self.resizable(0, 0)
        self._center_window(700, 400)

        self.main_frame = self._create_grid("25 25 25 25")
        
        self._configure_grid()
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
    
    def _start(self):
        # self.show_output()
        start(self)

    def _create_widgets(self):
        # PATH LABEL
        self.path_label = ttk.Label(self.main_frame, text="Music Files Location:")
        self.path_label.grid(row=0, column=0, sticky=(N, W), pady=5)

        # PATH ENTRY
        self.path       = StringVar()
        self.path_entry = ttk.Entry(self.main_frame, width=80, textvariable=self.path)
        self.path_entry.grid(row=0, column=1, columnspan= 2, sticky=(N, E), pady=5)

        # SUBDIR CHECKBUTTON
        self.subdir             = BooleanVar()
        self.sub_dir_ckeckbutton = ttk.Checkbutton(self.main_frame, text="Include Subdirectories", name="sub_dir", variable=self.subdir, onvalue=1, offvalue=0, state="normal")
        self.sub_dir_ckeckbutton.grid(row=1, column=1, columnspan= 2, sticky=(N, W), pady=5)

        # START BUTTON
        self.start_button = ttk.Button(self.main_frame, text="Start", width=20, command=self._start)
        self.start_button.grid(row=1, column=2, sticky=(N, E), pady=5)

        # OUTPUT TEXT
        self.output      = StringVar()
        self.output_text = tk.Text(self.main_frame, width=80, height=17, state=DISABLED)
        # self.output_text = ttk.Entry(self.main_frame, width=80, state=DISABLED)
        self.output_text.grid(row=2, column=0, columnspan=3, rowspan=3, sticky=NS, pady=5)

    def _configure_grid(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=3)

    # def show_output(self):
    #     self.output_text.configure(state=NORMAL)

    #     self.output_text.insert(END, self.subdir.get())

    #     self.output_text.configure(state=DISABLED)

    def get_subdir_value(self):
        return self.subdir.get()
    
    def set_output_value(self, output_value):
        self.output_text.configure(state=NORMAL)
        self.output_text.insert(END, output_value)
        self.output_text.configure(state=DISABLED)

if __name__ == "__main__":
    app = GUI()
    app.mainloop()
