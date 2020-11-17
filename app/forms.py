from django import forms

# 投稿フォーム
class TodoForm(forms.Form):
    title = forms.CharField(max_length=100, label='タイトル')
    # フォームで日付を選択したいため、widgetを使用する
    deadline = forms.DateField(widget=forms.DateInput(attrs={"type":'date'}), label='期限')
