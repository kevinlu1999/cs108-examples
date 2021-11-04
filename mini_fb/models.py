from django.db import models


# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    email_address = models.CharField(max_length=45)
    profile_image_url = models.URLField(blank=True)

    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.first_name, self.last_name, self.city, self.email_address, self.profile_image_url)

    def get_status_messages(self):
        return StatusMessage.objects.filter(profile=self)


class StatusMessage(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True)
    profile = models.ForeignKey('Profile', on_delete=models.CASCADE)

    def __str__(self):
        return '{}, {}, {}'.format(self.timestamp, self.message, self.profile)
