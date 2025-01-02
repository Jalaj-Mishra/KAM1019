from django.db import models

# Create your models here.
class Lead(models.Model):
    LEAD_TYPE = [
        ('BE', 'BikanerExpress'),
        ('BB', 'BikanerBistro'),
        ('BR', 'BikanerRestaurant'),
        ('BC', 'BikanerCafe'),
        ('BP', 'BikanerPizzeria'),
        ('BB', 'BikanerWale'),
    ]
    LEAD_STATUS = [
        ('OO', 'Open'),
        ('OC', 'On-Call'),
        ('CE', 'Close'),
        ('DE', 'Done'),
    ]
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40, primary_key=True)
    Mobile = models.CharField(max_length=13)
    LeadType = models.CharField(max_length=2, choices=LEAD_TYPE)
    LeadStatus = models.CharField(max_length=2, choices=LEAD_STATUS, default="OO")



    def __str__(self):
        return f'{self.name} - {self.LeadType} - {self.LeadStatus}'