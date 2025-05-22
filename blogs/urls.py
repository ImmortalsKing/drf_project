from django.urls import path
from . import views

urlpatterns = [
    path('list-create/', views.BlogListCreateApiView.as_view()),
    path('<pk>', views.BlogDetailsApiView.as_view()),
    path('comments/create/', views.CreateCommentApiView.as_view()),
    path('comments/<pk>', views.UpdateDeleteCommentApiView.as_view()),
    path('<int:blog_id>/comments/', views.SpecificBlogCommentsApiView.as_view()),
]