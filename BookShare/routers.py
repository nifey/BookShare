from rest_framework import routers
from books.api.viewsets import BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)