import tkinter as tk
import random

WIDTH = 900
HEIGHT = 450
BAR_WIDTH = 12

class SortApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Selection Sort Visualizer")

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#111")
        self.canvas.pack()

        self.values = []
        self.generate_values()

        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=10)

        tk.Button(self.btn_frame, text="Generate", command=self.generate_values).grid(row=0, column=0, padx=5)
        tk.Button(self.btn_frame, text="Sort", command=self.start_sort).grid(row=0, column=1, padx=5)

    def generate_values(self):
        self.values = [random.randint(20, HEIGHT) for _ in range(WIDTH // BAR_WIDTH)]
        self.draw()

    def draw(self, current=None, minimum=None, sorted_idx=None):
        self.canvas.delete("all")

        for i, val in enumerate(self.values):
            x0 = i * BAR_WIDTH
            y0 = HEIGHT - val
            x1 = (i + 1) * BAR_WIDTH
            y1 = HEIGHT

            color = "white"

            if sorted_idx and i < sorted_idx:
                color = "green"
            elif i == minimum:
                color = "blue"
            elif i == current:
                color = "red"

            self.canvas.create_rectangle(x0, y0, x1, y1, fill=color)

        self.root.update_idletasks()

    def selection_sort(self):
        n = len(self.values)

        for i in range(n):
            min_idx = i

            for j in range(i + 1, n):
                yield j, min_idx, i

                if self.values[j] < self.values[min_idx]:
                    min_idx = j
                    yield j, min_idx, i

            self.values[i], self.values[min_idx] = self.values[min_idx], self.values[i]
            yield i, min_idx, i

    def start_sort(self):
        self.generator = self.selection_sort()
        self.animate()

    def animate(self):
        try:
            current, minimum, sorted_idx = next(self.generator)
            self.draw(current=current, minimum=minimum, sorted_idx=sorted_idx)
            self.root.after(30, self.animate)
        except StopIteration:
            self.draw(sorted_idx=len(self.values))

root = tk.Tk()
app = SortApp(root)
root.mainloop()