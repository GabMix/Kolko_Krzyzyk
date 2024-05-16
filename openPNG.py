import tkinter as tk

def on_click():
    print("Clicked on button")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
image_path = "C:\\Users\\dagak\\OneDrive\\Pulpit\\1a778b59-a942-4350-8e97-f5b646f00e45.png"
#sciezka githubowa!!:
#https://github.com/GabMix/Kolko_Krzyzyk/blob/1-koncept-graficzny-interface/1a778b59-a942-4350-8e97-f5b646f00e45.jpg
photo = tk.PhotoImage(file=image_path)
label = tk.Label(frame, image=photo)
label.pack()
button = tk.Button(frame, text="Click me", command=on_click)
button.pack()
root.mainloop()
