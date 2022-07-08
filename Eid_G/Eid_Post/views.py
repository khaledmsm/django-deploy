from django.shortcuts import render
from .models import Name
from django.shortcuts import redirect
from PIL import Image,ImageDraw , ImageFont
from django.http import FileResponse,HttpResponse
# Create your views here.

def Home(request):
        ## name_input = str(request.POST.get('user_name'))

        """ img = Image.open("C:\\Users\\kmm\\Desktop\\my_django_stuff\\Eid_G\\files\\covers\\mypic.png")

        d = ImageDraw.Draw(img)

        fnt = ImageFont.truetype('C:\\Users\\kmm\\Desktop\\fonts\\static\Cairo-Bold.ttf',40)

        message = name_input

        d.text((540,1020),message, font=fnt, fill=(237, 185, 117),anchor="ms")

        img.save('Images/'+name_input+'.png')
        save_in_model = Name(massenger_name=name_input,image=name_input+'.png')

        save_in_model.save() """

        return render(request , 'index.html')

def Show(request):
        name_input = request.POST.get('user_name')
        if name_input is None:
            return redirect(Home)
        else:
            name_input = str(request.POST.get('user_name'))

            img = Image.open("C:\\Users\\kmm\\Desktop\\my_django_stuff\\Eid_G\\files\\covers\\mypic.png")

            d = ImageDraw.Draw(img)

            fnt = ImageFont.truetype('C:\\Users\\kmm\\Desktop\\fonts\\static\Cairo-Bold.ttf',40)

            message = name_input

            d.text((540,1020),message, font=fnt, fill=(237, 185, 117),anchor="ms")

            img.save('Images/'+name_input+'.png')
            save_in_model = Name(massenger_name=name_input,image=name_input+'.png')

            save_in_model.save()
            i_mg = open('Images/'+name_input+'.png','rb')

            return FileResponse(i_mg)
    #name_input = request.POST.get('user_name')

    #name_in_model = Name(massenger_name=name_input)
    #name_in_model.save()

    #return render(request , 'index.html')
