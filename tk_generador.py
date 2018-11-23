# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import Tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from numpy import arange,sin, pi

class ControlPanel(tk.Frame):
	def __init__(self,master):
		super(ControlPanel, self).__init__()
		self.grid()
		self.pack()
		self.create_widgets()

	def create_widgets(self):
		self.sin_btn = tk.Button(self)
		self.sin_btn["text"] = "Sin(α)"
		self.sin_btn.grid(row=0, column=0, padx=5, pady=5)
		#self.sin_btn.pack(side="top")

		self.cos_btn = tk.Button(self)
		self.cos_btn["text"] = "Cos(α)"
		self.cos_btn.grid(row=0, column=1, padx=5, pady=5)
		#self.cos_btn.pack(side="top")

		self.sqr_btn = tk.Button(self)
		self.sqr_btn["text"] = "Square(α)"
		self.sqr_btn.grid(row=0, column=2, padx=5, pady=5)
		#self.sqr_btn.pack(side="top")

		self.sawt_btn = tk.Button(self)
		self.sawt_btn["text"] = "Sawtooth(α)"
		self.sawt_btn.grid(row=1, column=0, padx=5, pady=5)
		#self.sawt_btn.pack(side="top")

		self.sawt_btn = tk.Button(self)
		self.sawt_btn["text"] = "Triangle(α)"
		self.sawt_btn.grid(row=1, column=1, padx=5, pady=5)
		#self.sawt_btn.pack(side="top")

		self.amp_slide = tk.Scale(self, from_=0, to=10, tickinterval=10, label="Amplitude", orient="horizontal", length=200)
		self.amp_slide.grid(row=2, column=0, columnspan=3)
		
		self.freq_slide = tk.Scale(self, from_=0, to=100, tickinterval=100, label="Frequency", orient="horizontal", length=200)
		self.freq_slide.grid(row=3, column=0, columnspan=3)
		self.pack()

class PlotPanel(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.create_plot()

	def create_plot(self):
		self.label = tk.Label(self, text="Plotting signal:")
		self.label.grid(row=1, column=0, padx=5, pady=5)
		
		f = plt.Figure(figsize=(5, 4), dpi=100)
		a = f.add_subplot(111)
		t = arange(0.0, 3.0, 0.01)
		s = sin(2*pi*t)
		a.plot(t, s)

		# a tk.DrawingArea
		canvas = FigureCanvasTkAgg(f, self.master)
		canvas.show()
		canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		toolbar = NavigationToolbar2TkAgg(canvas, self.master)
		toolbar.update()
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

		self.pack()

ro = tk.Tk()
usr = tk.Toplevel(ro)
ro.title("Control Panel")
usr.title("Plot")
app = ControlPanel(ro)
sub_app = PlotPanel(master=usr)
app.mainloop()