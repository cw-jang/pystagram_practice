from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

from .forms import PhotoForm

@login_required
def create_photo(request):
	if request.method == 'GET':
		form = PhotoForm()
	elif request.method == 'POST':
		form = PhotoForm(request.POST, request.FILES)
		if form.is_valid():
			photo = form.save(commit=False)
			photo.user = request.user
			photo.save()
			return redirect('photos:view_photo', photo.pk)

	return render(request, 'edit_photo.html', {
		'form': form, 
		})

@login_required
def view_photo(request, pk):
	return render(request, 'view_photo.html', {

		})