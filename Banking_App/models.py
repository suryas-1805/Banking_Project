from django.db import models

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    account_name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.account_name

class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    account_ptr = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,blank=True)

    def __str__(self):
        return self.customer_name

    class Meta:
        base_manager_name = 'objects'