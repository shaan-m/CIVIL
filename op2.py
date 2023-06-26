from PIL import Image, ImageDraw, ImageFont
import random

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

bhk = input("Enter bhk: ")
b = input("Enter dimension of bedroom 1: ")
b1 = input("Enter dimension of bedroom 2: ")
l = input("Enter dimension of living room: ")
k = input("Enter dimension of kitchen: ")
ba = input("Enter dimension of bathroom: ")

text = "Living room " + l
textt = "Bedroom " + b
texttt = "Bedroom " + b1
textttt = "Kitchen " + k
texttttt = "Bathroom " + ba

if bhk == '2':
    imag = Image.open("C:/Users/LYZEN/Downloads/Untitled.jpg")
    imagee=Image.open("C:/Users/LYZEN/Downloads/Untitledd.jpg")
    imageee=Image.open("C:/Users/LYZEN/Downloads/Untitleddd.jpg") 
    #random_function = random.choice([draw1(imag), draw2(imagee), draw3(imageee)]) 
    random_number = random.randint(1, 3)
    if random_number == 1:
        draw1(imag)
    elif random_number == 2:
        draw2(imagee)
    else:
        draw3(imageee)
