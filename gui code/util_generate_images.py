from PIL import Image, ImageDraw, ImageFont

texts = ['first 1', 'second 2', 'third 3', 'fourth 4', 'fifth 5', 'sixth 6', 'last 7']
colours = ['red', 'orange', (238,238,30), 'darkgreen', 'lightblue', 'midnightblue', 'purple']
SAVE_PATH = "SAVE_PATH"

width, height = 1000, 600
fontsize = 150
font = ImageFont.truetype('arial.ttf', fontsize)

for i in range(len(texts)):
    img = Image.new('RGB', (width, height), color='white')
    d = ImageDraw.Draw(img)
    d.text((width/2 - fontsize/2, height/2 - fontsize/2), texts[i], font=font, fill=colours[i])
    img.save(f"{SAVE_PATH}test_image {i+1}.png")
