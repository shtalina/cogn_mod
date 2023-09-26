from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.Stud),
    path('faculties', views.faculties, name='faculties'),
    path('<int:id>', views.profile, name='profile'),

    #path('cognitive_profile/', views.plot_cognitive_profile, name='cognitive_profile')

]
