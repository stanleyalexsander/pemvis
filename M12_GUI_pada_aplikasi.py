import tkinter as tk
from tkinter import ttk, colorchooser, messagebox


class ShapeDrawerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Drawer")
        self.root.geometry("600x600")

        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.shape = tk.StringVar(value="line")

        self.create_widgets()
        self.bind_events()

    def create_widgets(self):
        frame = ttk.Frame(self.root)
        frame.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(frame, text="Shape:").pack(side=tk.LEFT)
        ttk.Radiobutton(frame, text="Line", variable=self.shape, value="line").pack(side=tk.LEFT)
        ttk.Radiobutton(frame, text="Rectangle", variable=self.shape, value="rectangle").pack(side=tk.LEFT)
        ttk.Radiobutton(frame, text="Circle", variable=self.shape, value="circle").pack(side=tk.LEFT)

        self.color_frame = ttk.Frame(self.root)
        self.color_frame.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(self.color_frame, text="Color:").pack(side=tk.LEFT)
        self.color_var = tk.StringVar(value="red")
        colors = ["red", "green", "blue", "yellow", "magenta", "white"]
        for color in colors:
            ttk.Radiobutton(self.color_frame, text=color.capitalize(), variable=self.color_var, value=color).pack(side=tk.LEFT)

        self.fill_color_var = tk.StringVar(value="white")
        self.fill_color_frame = ttk.Frame(self.root)
        self.fill_color_frame.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(self.fill_color_frame, text="Fill Color:").pack(side=tk.LEFT)
        for color in colors:
            ttk.Radiobutton(self.fill_color_frame, text=color.capitalize(), variable=self.fill_color_var, value=color).pack(side=tk.LEFT)

        self.options_frame = ttk.Frame(self.root)
        self.options_frame.pack(side=tk.TOP, fill=tk.X)

        ttk.Label(self.options_frame, text="Line Width:").pack(side=tk.LEFT)
        self.line_width = tk.IntVar(value=2)
        ttk.Spinbox(self.options_frame, from_=1, to=10, textvariable=self.line_width).pack(side=tk.LEFT)

        self.create_coord_entries()

        ttk.Button(self.root, text="Draw", command=self.draw_shape).pack(side=tk.TOP, fill=tk.X)

    def create_coord_entries(self):
        self.coord_frame = ttk.Frame(self.root)
        self.coord_frame.pack(side=tk.TOP, fill=tk.X)

        self.coord_labels = []
        self.coord_entries = []
        coord_names = ["X1", "Y1", "X2", "Y2", "X3", "Y3", "X4", "Y4", "Radius"]
        for name in coord_names:
            label = ttk.Label(self.coord_frame, text=f"{name}:")
            label.pack(side=tk.LEFT)
            self.coord_labels.append(label)
            entry = ttk.Entry(self.coord_frame, width=5)
            entry.pack(side=tk.LEFT)
            self.coord_entries.append(entry)

        self.update_coord_entries()

    def bind_events(self):
        self.shape.trace_add("write", self.update_coord_entries)

    def update_coord_entries(self, *args):
        shape = self.shape.get()
        if shape == "line":
            for i, entry in enumerate(self.coord_entries):
                entry.config(state=tk.NORMAL if i < 4 else tk.DISABLED)
        elif shape == "rectangle":
            for i, entry in enumerate(self.coord_entries):
                entry.config(state=tk.NORMAL if i < 8 else tk.DISABLED)
        elif shape == "circle":
            for i, entry in enumerate(self.coord_entries):
                entry.config(state=tk.NORMAL if i < 3 or i == 8 else tk.DISABLED)

    def draw_shape(self):
        shape = self.shape.get()
        line_width = self.line_width.get()
        color = self.color_var.get()
        fill_color = self.fill_color_var.get()

        coords = []
        for entry in self.coord_entries:
            try:
                coords.append(float(entry.get()))
            except ValueError:
                coords.append(None)

        self.canvas.delete("all")
        if shape == "line":
            self.canvas.create_line(coords[0], coords[1], coords[2], coords[3], width=line_width, fill=color)
        elif shape == "rectangle":
            self.canvas.create_polygon(coords[0], coords[1], coords[2], coords[3], coords[4], coords[5], coords[6], coords[7], outline=color, fill=fill_color, width=line_width)
        elif shape == "circle":
            x1 = coords[0] - coords[8]
            y1 = coords[1] - coords[8]
            x2 = coords[0] + coords[8]
            y2 = coords[1] + coords[8]
            self.canvas.create_oval(x1, y1, x2, y2, outline=color, fill=fill_color, width=line_width)


if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeDrawerApp(root)
    root.mainloop()
