import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfile

class View(tk.Frame):
    count = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        tk.Button(self, text="open", command=self.open).pack(fill=tk.X)
        tk.Button(self, text="save", command=self.save).pack(fill=tk.X)
        tk.Button(self, text="run program", command=self.draw).pack(fill=tk.X)
        self.txt = tk.Text(self, height=30)
        scr = tk.Scrollbar(self)
        scr.config(command=self.txt.yview)
        self.txt.config(yscrollcommand=scr.set)
        scr.pack(side="right", fill="y", expand=False)
        self.txt.pack(side="left", fill="both", expand=True)
        self.pack()
    def draw(self, size=500):
        exec(str(self.txt.get(1.0, tk.END)))
        self.pixels = [[(0, 0, 0) for y in range(size)] for x in range(size)]
        self.pixels = render(self.pixels)
        window = tk.Toplevel(self)
        window.resizable(0,0)
        canvas = tk.Canvas(window, width=size, height=size, bg='white')
        canvas.pack()
        img = tk.PhotoImage(width=size, height=size)
        canvas.create_image((size/2, size/2), image=img, state="normal")
        for y in range(size):
            for x in range(size):
                img.put(self.rgbtohex(self.pixels[x][y]), (x,y))
        window.mainloop()
    def rgbtohex(self, rgb):
        return ("#" + "{:02X}" * 3).format(*rgb)
    def open(self):
        self.txt.delete(1.0, tk.END)
        self.txt.insert(tk.END, open(askopenfilename()).read())
    def save(self):
        f = asksaveasfile(mode='w', defaultextension=".py")
        if f is None:
            return
        text2save = str(self.txt.get(1.0, tk.END))
        f.write(text2save)
        f.close()

if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(0,0)
    main = View(root)
    root.mainloop()

