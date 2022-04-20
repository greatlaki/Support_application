from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('tickets', TicketList, basename='tickets')

urlpatterns = [
    path("", include(router.urls)),
    path('append_tickets/', AppendTicket.as_view(), name='append_tickets'),
    path('support_response/', ResponseList.as_view(), name='support_response'),
    path('details/', TicketDetail.as_view(), name='details'),
    path('register/', RegisterView.as_view()),
]