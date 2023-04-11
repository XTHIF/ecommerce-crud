from django.db import models

class Customer(models.Model):
    c_name = models.CharField(max_length = 50)
    c_email = models.CharField(max_length = 50)
    c_phone = models.CharField(max_length = 50)
    c_password = models.CharField(max_length = 50, default = '')

    class Meta:
        db_table = 'customer'

class Seller(models.Model):
    s_name = models.CharField(max_length = 50)
    s_email = models.CharField(max_length = 50)
    s_phone = models.CharField(max_length = 50)
    s_password = models.CharField(max_length = 50, default = '')

    class Meta:
        db_table = 'seller'

class Product(models.Model):
    m_name = models.CharField(max_length = 50)
    m_category = models.CharField(max_length = 50)
    m_price = models.CharField(max_length = 50)
    m_Seller = models.ForeignKey(Seller,on_delete = models.CASCADE)
    m_description = models.CharField(max_length = 200)
    images = models.ImageField(upload_to = 'product/', default='')



