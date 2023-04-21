from django.db import models

class Clothes_Categories(models.Model):

    class Meta:
        db_table = "Clothes_Categories"

    category_name = models.CharField(max_length=100)



class Clothes(models.Model):
    class Meta:
        db_table = "Clothes"

    name = models.CharField(max_length=200)
    company = models.CharField(max_length=100)
    size = models.CharField(max_length=20)
    price = models.IntegerField()
    color = models.CharField(max_length=20)
    material = models.CharField(max_length=100)
    photo1 = models.FileField(upload_to="cloth_pics")
    photo2 = models.FileField(upload_to="cloth_pics", null=True,blank=True)
    photo3 = models.FileField(upload_to="cloth_pics", null=True,blank=True)
    photo4 = models.FileField(upload_to="cloth_pics", null=True,blank=True)
    photo5 = models.FileField(upload_to="cloth_pics", null=True,blank=True)
    photo6 = models.FileField(upload_to="cloth_pics", null=True,blank=True)
    description = models.TextField()
    category = models.ForeignKey(Clothes_Categories,on_delete=models.CASCADE)

