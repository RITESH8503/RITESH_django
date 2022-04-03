from django.db import models

# Create your models here.


from django.forms import CharField


class ContactUs(models.Model):    
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    contact=models.IntegerField(default='+91', editable=True)

    class Meta:
        db_table = "contact"

# Create your models here.
