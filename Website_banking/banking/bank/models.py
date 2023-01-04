from django.db import models
class Place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()



class Team(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='picture')
    desc=models.TextField()
    def __str__(self):
      return self.name

class Applicationform(models.Model):
        name = models.CharField(max_length=250)
        email = models.CharField(max_length=250)
        dob = models.CharField(max_length=250)
        phn = models.CharField(max_length=250)
        gender = models.CharField(max_length=250)
        account = models.CharField(max_length=250)
        address = models.TextField()
        state = models.CharField(max_length=250)
        district = models.CharField(max_length=250)
        branch = models.CharField(max_length=250)
        materials = models.CharField(max_length=250)

        def __str__(self):
            return self.name