from django.db import models

# Create your models here.

class TestImage(models.Model):
    #name = models.CharField(max_length=20)
    picture = models.ImageField(upload_to = 'testPictures')

    def __str__(self):
        return self.picture
    

    def delete(self, *args, **kwargs):
        self.picture.delete()
        super().delete(*args, **kwargs)
