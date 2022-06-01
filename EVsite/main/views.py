from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(reqest):
	tasks = Task.objects.order_by('-id')
	return render(reqest, 'main/index.html',{'title': 'Страница отзывов', 'tasks': tasks})


def about(reqest):
	return render(reqest, 'main/about.html')


def create(request):
	error = ''
	if request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			error = 'Форма была неверной'

	form = TaskForm()
	context = {
		'form': form,
		'error': error
	}
	return render(request, 'main/create.html', context)