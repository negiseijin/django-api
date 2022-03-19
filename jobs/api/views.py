from rest_framework import generics

from jobs.models import JobOffer
from jobs.api.serializers import JobOfferSerializer


class ListView(generics.ListCreateAPIView):
    """
    一覧取得
    """
    queryset = JobOffer.objects.all().order_by('-id')
    serializer_class = JobOfferSerializer


class DetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    詳細取得
    """
    queryset = JobOffer.objects.all()
    serializer_class = JobOfferSerializer
