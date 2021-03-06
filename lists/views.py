from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from lists.models import Item, List
from lists.forms import ExistingListItemForm, ItemForm
User = get_user_model()

# Create your views here.
def home_page(request):
	return render(request, 'home.html', {'form': ItemForm()})

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	form = ExistingListItemForm(for_list=list_)
	if request.method == 'POST':
		form = ExistingListItemForm(for_list=list_, data=request.POST)
		if form.is_valid():
			form.save()
			return redirect(list_)

	return render(request, 'list.html', {'list': list_, "form": form})

def new_list(request):
	form = ItemForm(data=request.POST)
	if form.is_valid():
		list_ = List.objects.create()
		list_.owner = request.user
		list_.save()
		form.save(for_list=list_)
		return redirect(list_)
	else:
		return render(request, 'home.html', {"form": form})

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST['text'], list=list_)
	return redirect(f'/lists/{list_.id}/')

def my_lists(request, email):
	owner = User.objects.get(email=email)
	return render(request, 'my_lists.html', {'owner': owner})