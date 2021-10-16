from django.db import models

class Hotel(models.Model):
    booking_date = models.DateField()
    status = models.BooleanField(default=False)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
  		  return str(self.id)
