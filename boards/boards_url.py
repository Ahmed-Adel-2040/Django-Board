from django.urls import path
from . import views

urlpatterns = [
    path('', views.BoardListView.as_view(),name="home"),
    path('boards/<int:board_id>',views.boards_topic,name="boards_topic"),
    path('boards/<int:board_id>/new',views.new_topic,name="new_topic"),
    path('boards/<int:board_id>/topics/<int:topic_id>',views.topic_posts,name="topic_posts"),
    path('boards/<int:board_id>/topics/<int:topic_id>/reply/',views.reply_post,name="reply_post"),
    path('boards/<int:board_id>/topics/<int:topic_id>/post/<int:post_id>/edit',views.UpdatePost.as_view(),name="edit_post")
]