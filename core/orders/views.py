from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions, status, generics, parsers
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.contrib.auth import get_user_model
User = get_user_model()
from .serializers import OrderSerializer, SubjectSerializer, UrgencySerializer
from .models import Order


# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
	serializer_class = OrderSerializer
	parser_classes = [parsers.MultiPartParser, parsers.FormParser]

	def get_queryset(self):
		return Order.objects.filter(user=self.request.user)


