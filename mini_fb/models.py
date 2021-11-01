from django.db import models

# Create your models here.


class Profile(models.Model):
    '''Show the profile of an individual'''
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    email_address = models.CharField(max_length=45)
    profile_image_url = models.URLField(blank=True)

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.first_name, self.last_name, self.city, self.email_address, self.profile_image_url)
