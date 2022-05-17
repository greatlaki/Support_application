from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Ticket(models.Model):

    STATUS_CHOICES = [
        (1, "OK"),
        (2, "NO"),
        (3, "Frozen"),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=250)
    status = models.IntegerField(verbose_name='status of ticket', choices=STATUS_CHOICES, default=2)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
        ordering = ['-created_date']


class SupportResponse(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(verbose_name='Answer')
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        ordering = ['-created_date']

