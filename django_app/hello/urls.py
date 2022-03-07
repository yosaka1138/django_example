from django.urls import path
from .views import HelloView
from . import views

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
]
