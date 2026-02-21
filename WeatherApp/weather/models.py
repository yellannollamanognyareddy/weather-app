from django.db import models

# Create your models here.
class SearchHistory(models.Model):
    city=models.CharField(max_length=100)
    temp=models.FloatField(max_length=100)
    humidity=models.IntegerField(max_length=100)
    description=models.CharField(max_length=200)
    searched_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.city}"