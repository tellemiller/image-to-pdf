from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

directory = filedialog.askdirectory()
images = []

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        images.append(Image.open(directory + '/' + filename))
    else:
        continue

for image in images:
    images[images.index(image)] = image.convert('RGB')

if len(images) > 1:
    images[0].save(directory + '/mergedImages.pdf', save_all=True, append_images=images[1:])
else:
    images[0].save(directory + '/mergedImages.pdf', save_all=True)

answer = tkinter.messagebox.askyesno("Delete files?", "Do you want to delete the original image files?")

if answer:
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            os.remove(directory + '/' + filename)
