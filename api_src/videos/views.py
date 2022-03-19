from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .models import Video
from .permissions import IsOwnerOrReadOnly
from .serializers import VideoSerializer
from .pagination import CustomPagination


class ListCreateVideoAPIView(ListCreateAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = (filters.DjangoFilterBackend,)

    def perform_create(self, serializer):
        # Assign the user who created the video
        serializer.save(creator=self.request.user)


class RetrieveUpdateDestroyVideoAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]





