# from blog import views
# from django.urls import path

# urlpatterns = [
#     path('', views.PostList.as_view(), name='home'),
#     path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
# ]


from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PostList, name='home'),
    path('<slug:slug>/', views.PostDetail, name='post_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
