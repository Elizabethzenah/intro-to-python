from PIL import Image

img = Image .open("images/skin 3.jpg")

img2 = img.convert("L")

img2.save("images/black_white_skin 3.jpg")


          #pip freeze > requirements.txt

          #write text at the centre of an image

from PIL import Image, ImageDraw, ImageFont


image = Image.open("images/skin 3.jpg.jpg")

draw = ImageDraw.Draw(image)


font = ImageFont.truetype("arial.ttf", 40)


text = "Centered Text"


text_width, text_height = draw.textsize(text, font=font)


image_width, image_height = image.size


x = (image_width - text_width) // 2
y = (image_height - text_height) // 2


hello =font, fill="white", draw.text((x, y), text:("hello world")


image.save("outputs/skin 3.jpg")
image.show()

