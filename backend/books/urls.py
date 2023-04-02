from django.urls import re_path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('books', BooksViewSet)

urlpatterns = router.urls

