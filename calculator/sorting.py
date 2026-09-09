import tkinter as tk
import random

# Window setup
WIDTH = 800
HEIGHT = 400
BAR_WIDTH = 10

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting Visualizer")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
        self.canvas.pack()

        self.data = []
        self.rectangles = []

        self.generate_data()

        self.start_button = tk.Button(root, text="Start Sorting", command=self.start_sort)
        self.start_button.pack(pady=10)

    def generate_data(self):
        self.data = [random.randint(10, HEIGHT) for _ in range(WIDTH // BAR_WIDTH)]
        self.draw_data()

    def draw_data(self, highlight_indices=[]):
        self.canvas.delete("all")
        self.rectangles = []

        for i, value in enumerate(self.data):
            x0 = i * BAR_WIDTH
            y0 = HEIGHT - value
            x1 = (i + 1) * BAR_WIDTH
            y1 = HEIGHT

            color = "red" if i in highlight_indices else "white"
            rect = self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)
            self.rectangles.append(rect)

        self.root.update_idletasks()

    def bubble_sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n - i - 1):
                yield j, j + 1  

                if self.data[j] > self.data[j + 1]:
                    self.data[j], self.data[j + 1] = self.data[j + 1], self.data[j]
                    yield j, j + 1  

    def start_sort(self):
        self.generator = self.bubble_sort()
        self.animate()

    def animate(self):
        try:
            indices = next(self.generator)
            self.draw_data(highlight_indices=indices)
            self.root.after(0, self.animate)  
        except StopIteration:
            self.draw_data()

# Run app
root = tk.Tk()
app = SortingVisualizer(root)
root.mainloop()