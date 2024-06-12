from tkinter import *
from tkinter import  ttk
from tkinter import filedialog
from PIL import ImageTk, Image, ImageEnhance, ImageFilter
import os
         
#fungsi mengganti gambar
def LoadImg():
    global img, ori_img
    imgname = filedialog.askopenfilename(title="Load Image")
    if imgname:
        img = Image.open(imgname)
        img = img.resize((800, 700))
        ori_img = img.copy()  # Simpan gambar asli
        displayimage(img)

#buat display image
def displayimage(img):
    dispimage = ImageTk.PhotoImage(img)
    panel.configure(image=dispimage)
    panel.image = dispimage

#fungsi brightness
def brightness_callback(brightness_pos):
	brightness_pos = float(brightness_pos)
	global outputImage
	enhancer = ImageEnhance.Brightness(img)
	outputImage = enhancer.enhance(brightness_pos)
	displayimage(outputImage)
     
#fungsi contrast
def contrast_callback(contrast_pos):
	contrast_pos = float(contrast_pos)
	global outputImage
	enhancer = ImageEnhance.Contrast(img)
	outputImage = enhancer.enhance(contrast_pos)
	displayimage(outputImage)

#fungsi rotasi
def rotate_image(direction):
    global img
    if img is not None:
        if direction == 'Rotate Left':
            img = img.rotate(90, expand=True)
        elif direction == 'Rotate Right':
            img = img.rotate(-90, expand=True)
        elif direction == 'Rotate 90':
            img = img.rotate(90, expand=True)
        elif direction == 'Rotate 180':
            img = img.rotate(180, expand=True)
        displayimage(img)

#fungsi mirror
def mirror():
    global img
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    displayimage(img)



# fungsi reset image
def reset_image():
    global img, ori_img
    img = ori_img.copy()  # Kembalikan gambar ke keadaan asli
    displayimage(img)

# MAIN LOOP 
root = Tk()
root.title("Image Editor")

space=(" ")*215
# It retrieves the screen width of the user's display
screen_width=root.winfo_screenwidth()

# It retrieves the screen height of the user's display
screen_height = root.winfo_screenheight()

#Using an f-string to construct the window size in the 
#format width x height
root.geometry(f"{screen_width}x{screen_height}")

#frame atas (tempat slider brightness & contrass, load & save img)
frame_t = Frame(root, bg='grey', width=400, height=60)
frame_t.pack(side=TOP, fill=X)

#frame atas (tempat button)
frame_l = Frame(root, bg='white', width=350, height=300)
frame_l.pack(side=LEFT, fill=Y)

#canvas yang menampilkan gambar
frame_r = Frame(root, bg='lightgrey', width=400, height=400)
frame_r.pack(side=RIGHT, fill=BOTH, expand=True)

canvas = Canvas(frame_r, cursor="cross", bg="gray")
canvas.pack(fill=BOTH, expand=True, padx=10, pady=10)

#gambar awal
img = Image.open("logo.png")
img = img.resize((700, 700))
ori_img = img.copy()
panel = Label(canvas)
panel.grid(row=0, column=0, rowspan=12, padx=300, pady=20)
displayimage(img)

#load image button
btnLoadImg = Button(frame_t, text='Load Image', width=15, command=LoadImg, bg="#939393",activebackground="LIGHTBLUE")
btnLoadImg.configure(font=('poppins',11,'bold'),foreground='white')
btnLoadImg.place(x=10,y=15)

# button reset image
btnResetImg = Button(frame_t, text='Reset Image', width=15, command=reset_image, bg="#939393",activebackground="LIGHTBLUE")
btnResetImg.configure(font=('poppins', 11, 'bold'), foreground='white')
btnResetImg.place(x=180, y=15)

#slider untuk brightness
brightnessSlider = Scale(frame_t, label="Brightness", from_=0, to=2, orient=HORIZONTAL, length=200,
						resolution=0.1, command=brightness_callback, bg="#616E7C")
#initially, color position set to 1
brightnessSlider.set(1)
brightnessSlider.configure(font=('poppins',11),foreground='white')
brightnessSlider.place(x=1300,y=1)

#slider untuk contrast
brightnessSlider = Scale(frame_t, label="Contrast", from_=0, to=2, orient=HORIZONTAL, length=200,
						resolution=0.1, command=contrast_callback, bg="#616E7C")
#initially, color position set to 1
brightnessSlider.set(1)
brightnessSlider.configure(font=('poppins',11),foreground='white')
brightnessSlider.place(x=1070,y=1)

#dropdown rotasi
rotation_options = ["Rotate Left", "Rotate Right", "Rotate 90", "Rotate 180"]
selected_rotation = StringVar(frame_l)
selected_rotation.set('Rotation')  # default value
rotation_menu = OptionMenu(frame_l, selected_rotation, *rotation_options, command=rotate_image)
rotation_menu.configure(font=('poppins', 11))
rotation_menu.pack(padx=10, pady=10)

#button mirror
btnmirror = Button(frame_l, text='Mirror', width=10, command=mirror)
btnmirror.configure(font=('poppins', 11))
btnmirror.pack(padx=10, pady=10)

ori_img = None

root.mainloop()