from django.db import models

class Book(models.Model):                                           #table definition
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    pages=models.IntegerField()                                      #attributes or fields
    price=models.IntegerField()
    language=models.CharField(max_length=20)
    cover=models.ImageField(upload_to="images")
    pdf=models.FileField(upload_to="pdf")


    def __str__(self):
        return self.title



