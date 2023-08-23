import tkinter as tk
from tkinter import ttk,messagebox
import pymysql
from PIL import Image, ImageDraw, ImageFont
import random

text = ""
textt = ""
texttt = ""
textttt = ""
texttttt = ""
    
def login_success_window(root):
    success_window = tk.Toplevel(root)
    success_window.title("Image Generation")
    success_window.geometry('500x500')

    bhk_label = tk.Label(success_window, text="BHK:",font=('ProductSans-Regular',16))
    bhk_label.pack()

    bhk_entry = tk.Entry(success_window)
    bhk_entry.pack()

    b1_label = tk.Label(success_window, text="Dimension of bedroom 1:",font=('ProductSans-Regular',16))
    b1_label.pack()

    b1_entry = tk.Entry(success_window)
    b1_entry.pack()
    
    b2_label = tk.Label(success_window, text="Dimension of bedroom 2:",font=('ProductSans-Regular',16))
    b2_label.pack()

    b2_entry = tk.Entry(success_window)
    b2_entry.pack()
    
    l_label = tk.Label(success_window, text="Dimension of living room:",font=('ProductSans-Regular',16))
    l_label.pack()

    l_entry = tk.Entry(success_window)
    l_entry.pack()
    
    k_label = tk.Label(success_window, text="Dimension of kitchen:",font=('ProductSans-Regular',16))
    k_label.pack()

    k_entry = tk.Entry(success_window)
    k_entry.pack()
    
    ba_label = tk.Label(success_window, text="Dimension of bathroom:",font=('ProductSans-Regular',16))
    ba_label.pack()

    ba_entry = tk.Entry(success_window)
    ba_entry.pack()
    
    generate_button = tk.Button(success_window, text="Generate Image",font=('ProductSans-Regular',12), command=lambda: generate_images(
        bhk_entry.get(), b1_entry.get(), b2_entry.get(), l_entry.get(), k_entry.get(), ba_entry.get()
    ))
    generate_button.pack()
    
    exit_button = tk.Button(success_window, text="Exit", font=('ProductSans-Regular', 12), command=success_window.destroy)
    exit_button.pack()
    
def generate_images(bhk, b1, b2, l, k, ba):
    global text, textt, texttt, textttt, texttttt
    text = "Living room " + l
    textt = "Bedroom " + b1
    texttt = "Bedroom " + b2
    textttt = "Kitchen " + k
    texttttt = "Bathroom " + ba

    if bhk == '2':
        imag = Image.open("C:/Users/LYZEN/Documents/Codeblocks/CIVIL/Untitled.jpg")
        imagee = Image.open("C:/Users/LYZEN/Documents/Codeblocks/CIVIL/Untitledd.jpg")
        imageee = Image.open("C:/Users/LYZEN/Documents/Codeblocks/CIVIL/Untitleddd.jpg")

        random_number = random.randint(1, 3)
        if random_number == 1:
            draw1(imag)
        elif random_number == 2:
            draw2(imagee)
        else:
            draw3(imageee)    
    else:
        messagebox.showinfo("Generation error","Unable to generate image!");
def login():
    username = username_entry.get()
    password = password_entry.get()

    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="bratva",
        database="uj"
    )

    cursor = connection.cursor()

    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()

    connection.close()

    if user:
        messagebox.showinfo("Success", "Login successful!")
        login_success_window(root) 
    else:
        messagebox.showerror("Error", "Invalid login credentials.")

root = tk.Tk()
root.title("Login Application")
root.geometry('300x200')
root.resizable(False, False)
head = tk.Label(root, text='SIGN IN', fg='#000000', bg='white', font=('ProductSans-Regular',12,'bold'))
head.place(x=0, y=0)
username_label = tk.Label(root, text="Username:",font=('ProductSans-Regular',12))
username_label.place(x=200,y=200)
username_label.pack()

username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Password:",font=('ProductSans-Regular',12))
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login",font=('ProductSans-Regular',12), command=login)
login_button.pack()


def draw1(image):
    draw = ImageDraw.Draw(image)
    position = (1087, 353)
    positionn = (1330, 540)
    positionnn = (745, 258)
    positionnnn = (1350, 278)
    positionnnnn = (730, 500)
    font = ImageFont.truetype("C:/Users/LYZEN/Downloads/google-sans-cufonfonts/ProductSans-Regular.ttf", 24)
    font_color = (0, 0, 0)
    draw.text(position, text, font=font, fill=font_color)
    draw.text(positionn, textt, font=font, fill=font_color)
    draw.text(positionnn, texttt, font=font, fill=font_color)
    draw.text(positionnnn, textttt, font=font, fill=font_color)
    draw.text(positionnnnn, texttttt, font=font, fill=font_color)
    print("Image generated")
    image.save("c:/Users/LYZEN/Downloads/Hel1.jpg")
    image.show()

def draw2(image):
    draw = ImageDraw.Draw(image)
    position = (3105, 625)
    positionn = (2020, 644)
    positionnn = (2826, 1310)
    positionnnn = (4020, 1260)
    positionnnnn = (1904, 1329)
    font = ImageFont.truetype("C:/Users/LYZEN/Downloads/google-sans-cufonfonts/ProductSans-Regular.ttf", 40)
    font_color = (0, 0, 0)
    draw.text(position, text, font=font, fill=font_color)
    draw.text(positionn, textt, font=font, fill=font_color)
    draw.text(positionnn, texttt, font=font, fill=font_color)
    draw.text(positionnnn, textttt, font=font, fill=font_color)
    draw.text(positionnnnn, texttttt, font=font, fill=font_color)
    print("Image generated")
    image.save("c:/Users/LYZEN/Downloads/Hel2.jpg")
    image.show()

def draw3(image):
    draw = ImageDraw.Draw(image)
    position = (1117, 220)
    positionn = (880, 511)
    positionnn = (630, 215)
    positionnnn = (1314, 557)
    positionnnnn = (557, 514)
    font = ImageFont.truetype("C:/Users/LYZEN/Downloads/google-sans-cufonfonts/ProductSans-Regular.ttf", 20)
    font_color = (0, 0, 0)
    draw.text(position, text, font=font, fill=font_color)
    draw.text(positionn, textt, font=font, fill=font_color)
    draw.text(positionnn, texttt, font=font, fill=font_color)
    draw.text(positionnnn, textttt, font=font, fill=font_color)
    draw.text(positionnnnn, texttttt, font=font, fill=font_color)
    print("Image generated")
    image.save("c:/Users/LYZEN/Downloads/Hel3.jpg")
    image.show()
    
root.mainloop()
