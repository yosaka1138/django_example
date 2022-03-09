from django.urls import path
from . import views
from .views import FriendList, FriendDeteil

# # url/&msg=...のパターンの時
# urlpatterns = [
#     path("", views.index, name="index"),
# ]

# # url/id/nickname/のパターン
# urlpatterns = [
#     path("<int:id>/<nickname>/", views.index, name="index"),
# ]

urlpatterns = [
    path("", views.index, name="index"),
    path("create", views.create, name="create"),
    path("edit/<int:num>", views.edit, name="edit"),
    path("delete/<int:num>", views.delete, name="delete"),
    # as_viewをつけると，viewとして使用することができる(?)
    path("list", FriendList.as_view()),
    path("detail/<int:pk>", FriendDeteil.as_view()),
    path("find", views.find, name="find"),
    path("check", views.check, name="check"),
    path("<int:num>", views.index, name="index"),
]
