
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings 
from . import views
from .views import custom_logout

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('' , views.post_list , name='post-list'),
    path('post_form/' , views.create_post , name='create_post'),
    path('<int:post_id>/edit/' , views.edit_post, name='edit_post'),
    path('<int:post_id>/delete/' , views.delete_post, name='delete_post'),
    path('register/' , views.register , name='register'),
   

   
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

