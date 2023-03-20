from django.db import models

class Notification(models.Model):
    title = models.CharField(max_length=255,null=True)
    body = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    sent = models.BooleanField(default=False,null=True)