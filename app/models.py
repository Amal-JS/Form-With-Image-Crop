from django.db import models

# Create your models here.


class Photo(models.Model):
    image1 = models.ImageField(upload_to='form_images/',null=True,blank=True)
    image2 = models.ImageField(upload_to='form_images/',null=True,blank=True)
    image3 = models.ImageField(upload_to='form_images/',null=True,blank=True)

    name = models.CharField(max_length=19)
    def __str__(self) -> str:
        return self.name