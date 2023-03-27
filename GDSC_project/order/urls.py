from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='order-home'),
    path('order/<int:pk>/', PostDetailView.as_view(), name='order-detail'),
    path('order/new/', PostCreateView.as_view(), name='order-create'),
    path('order/<int:pk>/update/', PostUpdateView.as_view(), name='order-update'),
    path('order/<int:pk>/delete/', PostDeleteView.as_view(), name='order-delete'),
    path('order/favourite/', views.favourites, name='order-favourite'),
    path('updated/<int:id>/', views.favourite_add , name='order-favourite_add'),
    path('tag/<slug:tag_slug>', views.order_list, name='order-tag'),
    path('tag/search/', views.order_search, name='order-search')
    ]
