from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ("id", "author", "title", "desc", "status", "created_date")


class ResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = SupportResponse
        fields = ("id", "ticket", "author", "content", "created_date")



