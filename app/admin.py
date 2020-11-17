from django.contrib import admin
from .models import Todo

# 管理画面でデータを管理できる
admin.site.register(Todo)
