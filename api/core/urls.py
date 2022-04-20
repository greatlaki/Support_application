from django.urls import path

from .views import *

urlpatterns = [
    path('append_tickets/', AppendTicket.as_view(), name='append_tickets'),
    path('tickets_list/', TicketList.as_view(), name='tickets_list'),
    path('support_response/', ResponseList.as_view(), name='support_response'),
    path('details/', TicketDetail.as_view(), name='details'),
]