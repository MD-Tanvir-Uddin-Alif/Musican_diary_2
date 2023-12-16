from django.urls import path
from .import views

urlpatterns = [
    # path('add/',views.add_album,name="add_album"),
    path('add/',views.AddAlbumClassView.as_view(),name="add_album"),
    # path('edit/<int:id>',views.edit_album,name="edit_post"),
    path('edit/<int:id>',views.EditAlbumClassView.as_view(),name="edit_post"),
    # path('delete/<int:id>',views.delete_album,name="delete_post")
    path('delete/<int:id>',views.DeleteAlbumClassView.as_view(),name="delete_post"),
]