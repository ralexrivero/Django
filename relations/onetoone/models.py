from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    def __str__(self):
        return 'Restaurant name: {}, address: {}'.format(self.name, self.address)

class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    number_of_employees = models.IntegerField(default=1)

    def __str__(self):
        return 'Restaurant: {}, Address: {}, Employees: {}'.format(self.place.name, self.place.address, self.number_of_employees)
 