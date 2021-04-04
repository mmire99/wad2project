from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('Thread/<int:pk>/',views.ThreadDetailView.as_view(),name='detail-view'),
    path('Create-Thread/',views.AddThreadView.as_view(),name ='create-thread'),
    path('like/<int:pk>/',views.likeButton,name='like_post'),
    path('profile/',views.profile,name='profile'),
    path('Category/<str:category>/',views.Categories,name='categories'),
    path('Thread/<int:pk>/delete',views.DeleteThread.as_view(),name='delete_thread'),
]
