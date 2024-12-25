from django.db import models

# Create your models here.
class Leads(models.Model):
    RESTAURENT_LEAD_TYPE = [
        ('BE', 'BinaknerExpress'),
        ('BB', 'BinaknerBistro'),
        ('BR', 'BinaknerRestaurant'),
        ('BC', 'BinaknerCafé'),
        ('BP', 'BinaknerPizzeria'),
        ('BB', 'BikanerWala'),
    ]
    LEAD_STATUS = [
        ('OO', 'Open'),
        ('OC', 'On-Call')
        ('CE', 'Close'),
        ('DE', 'Done'),
    ]