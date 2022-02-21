from django.db import models

# Create your models here.
class ALL_Category(models.Model):
    STAT = [("Cybersecurity and IT reviews",'Cybersecurity and IT reviews'),
                ("IT Software and Solutions","IT Software and Solutions"),
                 ("IT Project consulting","IT Project consulting"),]
    category = models.CharField(choices=STAT, max_length=255,blank=True)
    
    def __str__(self):
        return str(self.category)
class Offers(models.Model):
    STATS = [("Service",'Service'),
                ("Solution","Solution")]
    name = models.CharField(max_length=1000, blank=True)
    types = models.CharField(choices=STATS, max_length=255,blank=True)
    description = models.TextField()
    group = models.ForeignKey(ALL_Category, on_delete=models.CASCADE,related_name="groups")
    
    def __str__(self):
        return str(self.name)
    
    