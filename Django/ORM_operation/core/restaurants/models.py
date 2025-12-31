from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Restaurants (models.Model):
    TypeChoices = {
        "S": "Small",
        "M": "Medium",
        "L": "Large",
    }

    
    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    data_opened = models.DateField()
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices)

    def __str__(self):
        return self.name
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"Rating : {self.rating}"