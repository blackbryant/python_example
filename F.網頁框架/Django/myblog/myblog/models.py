# title/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering =('-pub_date',)
    def __str__(self):
        return self.title


class NewTable(models.Model):
    bigint_f = models.BigIntegerField()
    bool_f = models.BooleanField()
    date_f = models.DateField(auto_now=True)
    char_f = models.CharField(max_length=20,unique=True)
    datetime_f =models.DateTimeField(auto_now_add=True)
    decimal_f = models.DecimalField(max_digits=10,decimal_places=2)
    float_f = models.FloatField(null=True)
    int_f = models.IntegerField(default=0)
    text_f =models.TextField()
    
    #選項用法
    SIZES={('S','Small'),('L','Large'),('M','Medium')}
    size_f = models.CharField(max_length=1,default='S', choices=SIZES)
    
    class Meta:
        db_table = 'new_table'
        ordering=('-int_f',)
        def __str__(self) -> str:
            return self.date_f

class Product(models.Model):
    #選項用法
    SIZES={('S','Small'),('L','Large'),('M','Medium')}
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1,default='S', choices=SIZES)
