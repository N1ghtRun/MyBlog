from django.urls import path

from .views import IndexView, SinglePostView, CategoryView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:category>/<slug:slug>/', SinglePostView.as_view(), name='post'),
    path('<slug:slug>/', CategoryView.as_view(), name='category'),
]
