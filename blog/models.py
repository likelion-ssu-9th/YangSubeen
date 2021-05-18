from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_Length=100)
    writer= models.CharField(max_Length=50)
    pub_date =models.DateTimeField()
    body = models. TextField()

    def __str__(self):
        return self.title
