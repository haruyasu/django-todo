from django.views.generic import View
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        todo_data = Todo.objects.order_by("deadline")

        return render(request, 'app/index.html', {
            'todo_data': todo_data
        })


class CreateView(View):
    def get(self, request, *args, **kwargs):
        form = TodoForm(request.POST or None)

        return render(request, 'app/create.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = TodoForm(request.POST or None)

        if form.is_valid():
            todo_data = Todo()
            todo_data.title = form.cleaned_data['title']
            todo_data.deadline = form.cleaned_data['deadline']
            todo_data.save()
            return redirect('index')

        return render(request, 'app/create.html', {
            'form': form
        })


class EditView(View):
    def get(self, request, *args, **kwargs):
        todo_data = Todo.objects.get(id=self.kwargs['pk'])
        form = TodoForm(
            request.POST or None,
            initial={
                'title': todo_data.title,
                'deadline': todo_data.deadline,
            }
        )

        return render(request, 'app/create.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = TodoForm(request.POST or None)

        if form.is_valid():
            todo_data = Todo.objects.get(id=self.kwargs['pk'])
            todo_data.title = form.cleaned_data['title']
            todo_data.deadline = form.cleaned_data['deadline']
            todo_data.save()
            return redirect('index')

        return render(request, 'app/create.html', {
            'form': form
        })


class DeleteView(View):
    def get(self, request, *args, **kwargs):
        todo_data = Todo.objects.get(id=self.kwargs['pk'])
        todo_data.delete()
        return redirect('index')

