from django.conf.urls import url
from . import views



urlpatterns = [
    url('^$', views.welcome, name='welcome'),
    url('^day/$', views.display_image, name='Today'),
    url(r'^photo/(\d+)', views.single_photo, name='singlePhoto'),
    url(r'^all/$', views.all_images, name='allImages'),
    url(r'^search/', views.search_results, name='search_results')
]
