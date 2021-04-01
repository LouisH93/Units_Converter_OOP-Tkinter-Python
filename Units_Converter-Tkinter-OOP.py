'''A simple tkinter app for calculatng unit conversions'''
import tkinter as tk
import tkinter.font as font
from tkinter import ttk


class RootWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title('Units Converter')
        self.geometry('250x265')
        self.resizable(0, 0)
        self.iconbitmap('ruler-icon.ico')
        self.columnconfigure(0, weight=1)
        self.default_font = font.nametofont('TkDefaultFont').configure(size=10)
        self.frames = dict()

        self.style = ttk.Style()
        self.style.theme_use('clam')

        container = ttk.Frame(self, padding=(30, 15))
        container.grid(row=0, column=0, sticky='EW')

        '''self parameter enables the root to act as controller for switching between frames'''
        from_metres = ConvertFromMetres(container, self) 
        from_metres.grid(row=0, column=0, sticky='NSEW')

        from_miles = ConvertFromMiles(container, self)
        from_miles.grid(row=0, column=0, sticky='NSEW')

        self.frames[ConvertFromMetres] = from_metres
        self.frames[ConvertFromMiles] = from_miles # {ConvertFromMetres: from_metres, ConvertFromMiles: from_miles}

        self.show_frame(ConvertFromMetres) # The first frame to be displayed


    def show_frame(self, container):
        '''Simple function to raise frames, enabling the user to switch between screens'''
        frame = self.frames[container]
        # frame dict has access to both classes calculate functions, enabling for keybinding of both frames
        self.bind('<Return>', frame.calculate) # Windows Enter key
        frame.tkraise()

        
class ConvertFromMetres(ttk.Frame):
    def __init__(self, root_window, controller, **kwargs):
        super().__init__(root_window, **kwargs)
        
        self.metres_value = tk.StringVar()
        self.feet_value = tk.StringVar()
        self.inches_value = tk.StringVar()
        self.cm_value = tk.StringVar()
        self.mm_value = tk.StringVar()


        # Widget configurations
        metres_label = ttk.Label(self, text='Metres:')
        metres_input = ttk.Entry(self, width=10, textvariable=self.metres_value, font=('Segoe UI', 10))
        feet_label = ttk.Label(self, text='Feet:')
        feet_display = ttk.Label(self, textvariable=self.feet_value)
        inches_label = ttk.Label(self, text='Inches:')
        inches_display = ttk.Label(self, textvariable=self.inches_value)
        centimetre_label = ttk.Label(self, text='Centimetres:')
        centimetre_display = ttk.Label(self, textvariable=self.cm_value)
        millimetre_label = ttk.Label(self, text='Millimetres:')
        millimetre_display = ttk.Label(self, textvariable=self.mm_value)
        calc_button = ttk.Button(self, text='Calculate', command=self.calculate)
        switch_frames_button = ttk.Button(self, text='Switch to miles conversion', command=lambda: controller.show_frame(ConvertFromMiles))


        # Widget grid configurations
        metres_label.grid(row=0, column=0, sticky='W')
        metres_input.grid(row=0, column=1, sticky='EW')
        metres_input.focus()
        feet_label.grid(row=1, column=0, sticky='W')
        feet_display.grid(row=1, column=1, sticky='EW')
        inches_label.grid(row=2, column=0, sticky='EW')
        inches_display.grid(row=2, column=1, sticky='EW')
        centimetre_label.grid(row=3, column=0, sticky='EW')
        centimetre_display.grid(row=3, column=1, sticky='EW')
        millimetre_label.grid(row=4, column=0, sticky='EW')
        millimetre_display.grid(row=4, column=1, sticky='EW')
        calc_button.grid(row=5, column=0, columnspan=2, sticky='EW')
        switch_frames_button.grid(row=6, column=0, columnspan=3, sticky='EW')


        # Widget grid components padx and y configurations
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
        

    def calculate(self, *args):
        '''Simple function to calculate the unit conversions. Try except has been added to avoid a ValueError
        if the calculate button is clicked or Enter key is pressed without a value having been inputted by the user.'''
        try:
            metres = float(self.metres_value.get())
            feet = metres * 3.28084
            inches = metres * 39.3700787
            centimetres = metres * 100
            millimetres = metres * 1000
            self.feet_value.set(f'{feet:.2f}')
            self.inches_value.set(f'{inches:.2f}')
            self.cm_value.set(f'{centimetres:.0f}')
            self.mm_value.set(f'{millimetres:.0f}')
        except ValueError:
            pass
         

class ConvertFromMiles(ttk.Frame):
    '''Copy and paste code from the ConvertFromMetres class, only difference is the units of measurement'''
    def __init__(self, root_window, controller, **kwargs):
        super().__init__(root_window, **kwargs)
        
        self.miles_value = tk.StringVar()
        self.kilometres_value = tk.StringVar()
        self.feet_value = tk.StringVar()


        miles_label = ttk.Label(self, text='Miles:')
        miles_input = ttk.Entry(self, width=10, textvariable=self.miles_value, font=('Segoe UI', 10))
        kilometres_label = ttk.Label(self, text='Kilometres: ')
        kilometres_display = ttk.Label(self, textvariable=self.kilometres_value)
        feet_label = ttk.Label(self, text='Feet:')
        feet_display = ttk.Label(self, textvariable=self.feet_value)
        calc_button = ttk.Button(self, text='Calculate', command=self.calculate)
        switch_frames_button = ttk.Button(self, text='Switch to metres conversion', command=lambda: controller.show_frame(ConvertFromMetres))


        miles_label.grid(row=0, column=0, sticky='W')
        miles_input.grid(row=0, column=1, sticky='EW')
        miles_input.focus()
        kilometres_label.grid(row=1, column=0, sticky='EW')
        kilometres_display.grid(row=1, column=1, sticky='EW')
        feet_label.grid(row=3, column=0, sticky='EW')
        feet_display.grid(row=3, column=1, sticky='EW')
        calc_button.grid(row=4, column=0, columnspan=2, sticky='EW')
        switch_frames_button.grid(row=5, column=0, columnspan=3, sticky='EW')


        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
        

    def calculate(self, *args):
        try:
            miles = float(self.miles_value.get())
            kilometres = miles * 1.609
            feet = miles * 5280
            self.kilometres_value.set(f'{kilometres:.4f}')
            self.feet_value.set(f'{feet:.2f}')
        except ValueError:
            pass
        

root = RootWindow()
root.mainloop()
