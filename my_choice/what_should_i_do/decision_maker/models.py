from django.db import models

class DecisionOption(models.Model):
    category = models.CharField(max_length=100)
    option = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.option
