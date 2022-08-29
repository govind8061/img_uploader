from django.shortcuts import render
from .models import UploadImage
from .forms import UploadImageForm
# Create your views here.

def index(request):
	fn=UploadImageForm()
	if request.method == 'POST':
		fn=UploadImageForm(request.POST, request.FILES)
		if fn.is_valid():
			fn.save()
	img=UploadImage.objects.all()
	return render(request, 'index.html', {'form':fn,'img':img})