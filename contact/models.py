from django.db import models

class Info(models.Model):
    place = models.CharField(max_length=55)
    phone_no = models.CharField(max_length=22)
    email = models.EmailField(max_length=255)


    class Meta:
        verbose_name = ('info')
        verbose_name_plural = ('infos')

    def __str__(self):
        return self.email
