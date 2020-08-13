from django.urls import path
from django.views.generic import TemplateView
from things import views

app_name='things'
urlpatterns=[
    path('',views.index,name='index'),
    path('about/',TemplateView.as_view(template_name='things/gallery.html'),name='about'),
    path('<int:item_id>',views.detail,name='detail'),
    path('',views.item,name='item'),
    path('',views.req,name='req'),
    path('register/',views.register,name='register'),
    path('registerd/',views.registerd,name='registerd'),
    path('user_login/',views.user_login,name='user_login'),
    path('',views.create_item,name='create_item'),
    path('',views.add_item,name='add_item'),
    path('satreq/<int:id>/',views.delete_item,name='delete_item'),
    path('satreq2/<int:id>/',views.delete_item2,name='delete_item2'),
]
