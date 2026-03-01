from django.db import models

class Commo(models.Model):
    device_id = models.CharField(max_length=100)
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'commos'