from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()
    
    def __str__(self) -> str:
        return f"{self.name} : {str(self.no_of_guests)}"
    

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventories = models.IntegerField()
    
    def __str__(self):
        return f'{self.Title} : {str(self.price)}'
