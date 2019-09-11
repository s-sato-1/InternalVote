from django.db import models
from django.utils import timezone

# ====================================================

class Award(models.Model):
    """ Award Loging
    """
    # Award
    AWARD_CHOICES = (              
        ('Freshers', 'Freshers'),   
        ('Growth', 'Growth'),      
        ('Evolution', 'Evolution'),
        ('Reader', 'Reader'),      
    )                              
    award_text = models.CharField(max_length=20, choices=AWARD_CHOICES)

    # Employment
    EMP_CHOICES = (
        ('Regular', 'Regular'),
        ('Part-time', 'Part-time'),
        ('Group', 'Group'),
    )
    employment_text = models.CharField(max_length=10, choices=EMP_CHOICES)
    
    # PrizeWinner
    PERSON_CHOICES = (
    )
    prizewinner_text = models.CharField(max_length=20) # choices=PERSON_CHOICES

    # Reason
    reason_text = models.CharField(max_length=100)

    # Create Date
    create_date = models.DateTimeField(default=timezone.now)
   
class AwardMst(models.Model):
    """ Award Description 
    """
    # Award
    award_mst_text = models.CharField(max_length=20)

    # Discription
    discription_text = models.CharField(max_length=100) 

