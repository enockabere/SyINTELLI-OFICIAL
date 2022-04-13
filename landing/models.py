from django.db import models

# Create your models here.
class Category(models.Model):
    STAT = [("Cybersecurity and IT reviews",'Cybersecurity and IT reviews'),
                ("IT Software and Solutions","IT Software and Solutions"),
                 ("IT Project consulting","IT Project consulting"),]
    Category = models.CharField(choices=STAT, verbose_name="Category", max_length=255,blank=True)
    
    class  Meta: 
        verbose_name_plural  =  "Service & Product Category"
    
    def __str__(self):
        return str(self.Category)
class Offers(models.Model):
    STATS = [("Service",'Service'),
                ("Solution","Solution")]
    Name = models.CharField(max_length=1000, verbose_name="Service/Product Name", blank=True)
    Types = models.CharField(choices=STATS, verbose_name="Service/Product Type", max_length=255,blank=True)
    Description = models.TextField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name="groups")
    
    class  Meta: 
        verbose_name_plural  =  "Service & Products"
    
    def __str__(self):
        return str(self.Name)
    
    