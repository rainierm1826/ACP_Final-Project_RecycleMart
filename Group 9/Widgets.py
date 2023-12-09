import customtkinter

class Label(customtkinter.CTkLabel):
    def __init__(self, master, height, width, text, image, fg_color, bg_color, text_color, font, x, y):
        super().__init__(master=master,
                         height=height,
                         width=width,
                         text=text,
                         image=image,
                         fg_color=fg_color,
                         bg_color=bg_color,
                         text_color=text_color,
                         font=font)
        self.place(x=x, y=y)

class Frame(customtkinter.CTkFrame):
    def __init__(self, master, height, width, fg_color, border_color, border_width, corner_radius, x, y):
        super().__init__(master=master,
                         height=height,
                         width=width,
                         border_color=border_color,
                         corner_radius=corner_radius,
                         border_width=border_width,
                         fg_color=fg_color)
        self.place(x=x, y=y)

class Button(customtkinter.CTkButton):
    def __init__(self, master, height, width, image, text, bg_color, fg_color, hover_color, border_color, x, y, command):
        super().__init__(master=master,
                         height=height,
                         width=width,
                         image=image,
                         text=text,
                         bg_color=bg_color,
                         fg_color=fg_color,
                         hover_color=hover_color,
                         border_color=border_color,
                         command=command)
        self.place(y=y, x=x)

class Entry(customtkinter.CTkEntry):
    def __init__(self, master, height, width, fg_color, border_color, bg_color, text_color, placeholder_text,
                 placeholder_text_color, x, y):
        super().__init__(master=master,
                         height=height,
                         width=width,
                         fg_color=fg_color,
                         border_color=border_color,
                         bg_color=bg_color,
                         text_color=text_color,
                         placeholder_text=placeholder_text,
                         placeholder_text_color=placeholder_text_color)
        self.place(x=x, y=y)

class Menu(customtkinter.CTkOptionMenu):
    def __init__(self, master, values, corner_radius, width, text_color, dropdown_text_color, dropdown_hover_color,
                 state, fg_color, button_color, height, bg_color, variable, x, y):
        super().__init__(
            master=master,
            bg_color=bg_color,
            values=values,
            corner_radius=corner_radius,
            width=width,
            variable=variable,
            text_color=text_color,
            height=height,
            dropdown_text_color=dropdown_text_color,
            dropdown_hover_color=dropdown_hover_color,
            fg_color=fg_color,
            state=state,
            button_color=button_color
        )
        self.place(x=x, y=y)









