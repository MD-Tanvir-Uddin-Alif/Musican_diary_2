from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # path('add/',views.add_musician,name="add_musician"),
    path('add/',views.AdMusicanView.as_view(),name="add_musician"),
    # path('edit/<int:id>',views.edit_musician,name="edit_musician"),
    path('edit/<int:id>',views.EditMusicanView.as_view(),name="edit_musician"),
    path('signup/',views.user_signup,name="signup"),
    path('login/',views.UserLoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),

]