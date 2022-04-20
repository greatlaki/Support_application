from rest_framework import generics

from .models import *
from .serializers import *


class AppendTicket(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketList(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class ResponseList(generics.ListAPIView):
    queryset = SupportResponse.objects.all()
    serializer_class = ResponseSerializer


class TicketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer