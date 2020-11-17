from django.views.generic import View
from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm

# トップページ
class IndexView(View):
    # 画面読み込み
    def get(self, request, *args, **kwargs):
        # ToDoデータベースからデータを取得
        # 期限順に並び替え
        todo_data = Todo.objects.order_by("deadline")
        # フォームを取得
        form = TodoForm(request.POST or None)

        # テンプレートにデータを渡す
        return render(request, 'app/index.html', {
            'todo_data': todo_data,
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = TodoForm(request.POST or None)

        # フォームのバリデーション
        if form.is_valid():
            # 新規にデータベースを作成
            todo_data = Todo()
            # フォームからユーザが入力したタイトルを取得
            todo_data.title = form.cleaned_data['title']
            # フォームからユーザが入力した期限を取得
            todo_data.deadline = form.cleaned_data['deadline']
            # データベースに保存
            todo_data.save()

        # トップページにリダイレクト
        return redirect('index')


class EditView(View):
    def get(self, request, *args, **kwargs):
        # ToDoデータベースから編集したいToDoのidでフィルタリング
        todo_data = Todo.objects.get(id=self.kwargs['pk'])
        # フォームに初期値を設定
        form = TodoForm(
            request.POST or None,
            initial={
                'title': todo_data.title,
                'deadline': todo_data.deadline,
            }
        )

        # テンプレートにデータを渡す
        return render(request, 'app/edit.html', {
            'form': form
        })

    def post(self, request, *args, **kwargs):
        form = TodoForm(request.POST or None)

        if form.is_valid():
            # ToDoデータベースから特定のIDを取得して、内容を書き換える
            todo_data = Todo.objects.get(id=self.kwargs['pk'])
            todo_data.title = form.cleaned_data['title']
            todo_data.deadline = form.cleaned_data['deadline']
            todo_data.save()
            return redirect('index')

        return redirect('edit', self.kwargs['pk'])


class DeleteView(View):
    def get(self, request, *args, **kwargs):
        # ToDoデータベースから特定のIDを取得して、内容を削除する
        todo_data = Todo.objects.get(id=self.kwargs['pk'])
        todo_data.delete()
        return redirect('index')
