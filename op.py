from PIL import Image, ImageDraw, ImageFont

def draw1(a):
    draw = ImageDraw.Draw(a)
    draww= ImageDraw.Draw(a)
    drawww=ImageDraw.Draw(a)
    drawwww=ImageDraw.Draw(a)
    drawwwww=ImageDraw.Draw(a)
    # Define the text content and its position on the image

    position = (1087, 353)  # (x, y) coordinates of the text
    positionn = (1330, 540)
    positionnn = (745, 258)
    positionnnn = (1350, 278)
    positionnnnn= (730,500)
    # Define the font properties
    font_size = 24
    font_color = (0, 0, 0)  # RGB color value
    font = ImageFont.truetype("C:/Users/LYZEN/Downloads/google-sans-cufonfonts/ProductSans-Regular.ttf", 24)  # Specify the path to the font file

    # Add the text to the image
    draw.text(position, text, font=font, fill=font_color)
    draww.text(positionn, textt, font=font, fill=font_color)
    drawww.text(positionnn, texttt, font=font, fill=font_color)
    drawwww.text(positionnnn, textttt, font=font, fill=font_color)
    drawwwww.text(positionnnnn, texttttt, font=font, fill=font_color)
    print("Image generated ")
    # Save the modified image
    image.save("c:/Users/LYZEN/Downloads/Hel.jpg")



def draw2(a):
    draw = ImageDraw.Draw(a)
    draww= ImageDraw.Draw(a)
    drawww=ImageDraw.Draw(a)
    drawwww=ImageDraw.Draw(a)
    drawwwww=ImageDraw.Draw(a)

    # Define the text content and its position on the image

    position = (1087, 353)  # (x, y) coordinates of the text
    positionn = (1330, 540)
    positionnn = (745, 258)
    positionnnn = (1350, 278)
    positionnnnn= (730,500)
    # Define the font properties
    font_size = 24
    font_color = (0, 0, 0)  # RGB color value
    font = ImageFont.truetype("C:/Users/LYZEN/Downloads/google-sans-cufonfonts/ProductSans-Regular.ttf", 24)  # Specify the path to the font file

    # Add the text to the image
    draw.text(position, text, font=font, fill=font_color)
    draww.text(positionn, textt, font=font, fill=font_color)
    drawww.text(positionnn, texttt, font=font, fill=font_color)
    drawwww.text(positionnnn, textttt, font=font, fill=font_color)
    drawwwww.text(positionnnnn, texttttt, font=font, fill=font_color)
    print("Image generated ")
    # Save the modified image
    image.save("c:/Users/LYZEN/Downloads/Hel.jpg")
    image.show()

##############################################################################################
bhk=input("Enter bhk: ")

b=input("Enter dimension sof bedroom 1 :")
b1=input("Enter dimension of bedroom 2 :")
l=input("Enter dimension of living room : ")
k=input("Enter dimension of kitchen : ")
ba=input("Enter dimension of bathroom : ")

text="Living room "+l
textt="Bedroom "+b
texttt="Bathroom "+ba
textttt="Kitchen "+k
texttttt="Bedroom "+b1


#Condition defined should be here
if bhk == 2:
    image = Image.open("C:/Users/LYZEN/Downloads/Untitled.jpg")
    imagee=Image.open("C:/Users/LYZEN/Downloads/Untitledd.jpg")
    imageee=Image.open("C:/Users/LYZEN/Downloads/Untitleddd.jpg")    
    draw1(image)
else:  
    image = Image.open("C:/Users/LYZEN/Downloads/Untitled.jpg")
    draw2(image)