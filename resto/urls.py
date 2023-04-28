from django.conf import settings
from django.urls import path,include
from rest_framework import routers
from MaidaGrill.settings import STATIC_URL
from django.conf.urls.static import static
from resto.views import categViewSet, productViewSet, unitViewSet
 


router=routers.DefaultRouter()
router.register(r'categProd',categViewSet)
router.register(r'unitProd',unitViewSet)
router.register(r'Prod',productViewSet)

urlpatterns=[
      path('',include(router.urls)),
      path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)