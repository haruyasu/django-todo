from django.urls import path
from app import views

urlpatterns = [
    # トップページのURL
    path('', views.IndexView.as_view(), name='index'),
    # 編集ボタンを押した時のURL
    path('<int:pk>/edit/', views.EditView.as_view(), name='edit'),
    # 完了ボタンを押した時のURL
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
]
