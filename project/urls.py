from django.contrib import admin
from django.urls import path, include
from django.urls import include, re_path

urlpatterns = [
	#path('grappelli/', include('grappelli.urls')), 
    path('', include('afiliados.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
