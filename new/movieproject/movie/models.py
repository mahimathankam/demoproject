from django.db import models
class Movie(models.Model):
    name=models.CharField(max_length=30)
    desc=models.CharField(max_length=100)
    year=models.IntegerField()
    img=models.ImageField(upload_to='movie/img',null=True,blank=True)

    def __str__(self):
        return self.name
