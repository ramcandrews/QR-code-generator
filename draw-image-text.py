from PIL import Image, ImageDraw, ImageFont

import secrets

img = Image.new('RGB', (4000, 2000), color = 'white') # or (RRR, GGG, BBB)

fnt = ImageFont.truetype(secrets.font_dir + secrets.the_font, 896) # font size

d = ImageDraw.Draw(img)

d.text((50, 400), "HIGH DEF", font=fnt, fill = "black") # position of top left corner of text.

img.save('test-HD.png')
