from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlockListView.as_view(), name='home'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name="post_detail")
]

