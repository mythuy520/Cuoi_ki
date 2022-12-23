import sys
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import filedialog, ttk
import cv2
from threading import Thread
import numpy as np
import os
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
from tensorflow.keras.utils import load_img, img_to_array
from keras.preprocessing.image import ImageDataGenerator

root = tk.Tk()
root.geometry('500x600')
root.title("NHẬN DIỆN NHẠC CỤ CỔ TRUYỀN VIỆT NAM")


class ImageConverter(tk.Frame):
	def __init__(self, root):
		super().__init__(root)
		self.init_ui()

	def init_ui(self):
		self.pack()
		self.lable = tk.Label(self, text='NHẠC CỤ VIỆT NAM', font='arial 20', bg="lavender", fg="darkred")
		self.lable.pack()
		self.openbtn = tk.Button(self, text='Tải ảnh lên', fg="black", bg="white", font='arial 12',
								 command=self.open_image)
		self.openbtn.pack()
		# self.imageframe= tk.LabelFrame(self, text=' Image view')
		# self.imageframe.pack()
		self.lableimage = tk.Label(self, width=100, height=27)
		self.lableimage.pack()
		self.run1 = tk.Button(self, text='Nhận diện', fg="white", bg="light blue", font='arial 12',
							  command=self.nhandien)
		self.run1.place(x=80, y=420)

		self.openbtn1 = tk.Button(self, text='Xóa', fg="white", bg="darkred", font='arial 12', command=self.clear)
		self.openbtn1.place(x=200, y=420)

	def nhandien(self):
		model = load_model('nhac.h5')
		img5 = load_img(self.filemane, target_size=(150, 150))
		plt.imshow(img5)
		img5 = img_to_array(img5)
		img5 = img5.astype('float32')
		img5 = img5 / 255
		img5 = np.expand_dims(img5, axis=0)
		result = model.predict(img5)
		class_nhaccu = ['Cồng chiêng', 'Đàn gáo', "Đàn T'rưng", 'Đàn bầu', 'Đàn đá', 'Đàn đáy', 'Đàn đoản',
						'Đàn nguyệt','Đàn sến', 'Đàn tranh', 'Đàn tỳ bà', 'Khèn', 'Sáo trúc', 'Sênh tiền', 'Song loan', 'Trống']
		a = int(np.argmax(model.predict(img5), axis=1))
		print("Đây là nhạc cụ:", class_nhaccu[a])
		self.lable2 = tk.Label(self, text=class_nhaccu[a], bg="black", fg='white', font='arial 16')
		self.lable2.pack()

	def clear(self):
		self.lable2.destroy()

	def open_image(self):
		self.filemane = filedialog.askopenfilename()
		self.img = Image.open(self.filemane)
		self.x = int(self.img.size[0])
		self.y = int(self.img.size[1])
		self.img2 = self.img.resize((self.x, self.y))
		self.imgtk = ImageTk.PhotoImage(self.img)
		self.lableimage.config(image=self.imgtk, width=300, height=400)


gui = ImageConverter(root)

root.mainloop()
