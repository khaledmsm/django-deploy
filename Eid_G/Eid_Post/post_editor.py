from PIL import Image,ImageDraw , ImageFont
from .models import Name
img = Image.open("C:\Users\kmm\Desktop\my_django_stuff\Eid_G\files\covers")

d = ImageDraw.Draw(img)

fnt = ImageFont.truetype('C:\\Users\\kmm\\Desktop\\fonts\\static\\Cairo-Bold.ttf',40)

message = Name.massenger_name

d.text((540,1020),message, font=fnt, fill=(237, 185, 117),anchor="ms")

img.save('uploaded.png')

image_in_model = Name(image='uploaded.png')
image_in_model.save()
