import tkinter as tk

def on_click(event):
    x = event.x // square_size
    y = event.y // square_size
    print(f"Clicked on cell ({x}, {y})")

root = tk.Tk()

#zmiencie sciezke!!!
image_path = "C:\\Users\\dagak\\OneDrive\\Pulpit\\conceptart.png"
image = tk.PhotoImage(file=image_path)
#wymiar
image_width = image.width()
image_height = image.height()
#liczba kwadratow numerxnumer
squares_x = 3
squares_y = 3
# rozmiar kwadrat
square_size = min(image_width, image_height) // max(squares_x, squares_y)
#tlo jest obrazem naszym
canvas = tk.Canvas(root, width=image_width, height=image_height)
canvas.pack()
#dziwna funkcja ze stacka
canvas.create_image(0, 0, anchor=tk.NW, image=image)
# linie
for i in range(1, squares_x):
    x = i * square_size
    canvas.create_line(x, 0, x, image_height, fill="black")

for j in range(1, squares_y):
    y = j * square_size
    canvas.create_line(0, y, image_width, y, fill="black")
# Dodanie obslugi zdarzeń kliknięcia
canvas.bind("<Button-1>", on_click)

root.mainloop()
