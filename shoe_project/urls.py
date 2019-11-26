from django.urls import include, path
from rest_framework import routers
from shoe_project.shoe_app import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'shoe', views.ShoeViewSet)
router.register(r'shoe_type', views.ShoeTypeViewSet)
router.register(r'shoe_color', views.ShoeColorViewSet)
router.register(r'manufacturer', views.ManufacturerViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]