from django.shortcuts import render
import qrcode
import qrcode.image.svg
from io import BytesIO
# Create your views here.
def home(request):
    factory = qrcode.image.svg.SvgImage
    qr_text = f'Nepal Pharmacy Council:  is registered'

    img = qrcode.make(qr_text, image_factory=factory, box_size=8)
    stream = BytesIO()
    img.save(stream)
    svg = stream.getvalue().decode()
    return render(request,'home.html',locals())