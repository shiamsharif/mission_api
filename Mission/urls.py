from rest_framework import routers

from Mission import views


router = routers.DefaultRouter()
router.register(r'', views.MissionViewSet, basename='mission')


urlpatterns = router.urls