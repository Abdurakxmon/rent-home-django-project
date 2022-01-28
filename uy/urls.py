from django.urls import path
from .import views

app_name='uy'

urlpatterns = [
	path('', views.home, name='home'),
	path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('logout_acces/',views.logout_s, name='logoutacc'),
    path('uy/', views.ijaraga_uy, name="ijara"),
    path('uy_qoyish/',views.ijaraga_uy_qoyish, name="qoyish"),
    path('home/<int:id>/', views.PostViewDetail.as_view(), name='home_detail'),
    path('results/', views.FilterPostsView.as_view(), name='serch_homes'),

]