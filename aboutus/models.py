from django.db import models

# Create your models here.
class AboutUs(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()

    class Meta:
        verbose_name = ("Aboutus")
        verbose_name_plural = ("Aboutus")

    def __str__(self):
        return self.title

class Why_Choose_Us(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()

    class Meta:
        verbose_name = ("Why_Choose_Us")
        verbose_name_plural = ("Why_Choose_Us")

    def __str__(self):
        return self.title

class Chef(models.Model):
    name=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    bio=models.TextField()
    image=models.ImageField(upload_to='chef/')

    class Meta:
        verbose_name = ("Chef")
        verbose_name_plural = ("Chef")

    def __str__(self):
        return self.name