import csv
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def read_csv_file():
    filename = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])
    if filename:
        with open(filename, newline='') as f:
            reader = csv.reader(f)
            data = list(reader)
            treeview.delete(*treeview.get_children())
            columns = data[0]  # Ambil header dari dataset
            treeview["columns"] = columns
            for column in columns:
                treeview.column(column, width=100)
                treeview.heading(column, text=column)
            for row in data[1:]:  # Skip header, mulai dari baris ke-2
                treeview.insert('', 'end', values=row)


def show_graph():
    # Ambil data dari treeview
    data = []
    for child in treeview.get_children():
        data.append(treeview.item(child)['values'])

    # Buat grafik batang
    figure = plt.Figure(figsize=(6, 5), dpi=100)
    ax = figure.add_subplot(111)
    ax.bar([row[0] for row in data], [row[1] for row in data])
    ax.set_title("Grafik Batang dari CSV File")
    ax.set_xlabel("X Axis")
    ax.set_ylabel("Y Axis")

    # Tampilkan grafik pada GUI
    canvas = FigureCanvasTkAgg(figure, root)
    canvas.get_tk_widget().pack(pady=10)


root = tk.Tk()
root.title("CSV Reader")

button = tk.Button(root, text="Select CSV file", command=read_csv_file)
button.pack(pady=10)

treeview = ttk.Treeview(root, show="headings")
treeview.pack(pady=10)

graph_button = tk.Button(root, text="Show Graph", command=show_graph)
graph_button.pack(pady=10)

root.mainloop()