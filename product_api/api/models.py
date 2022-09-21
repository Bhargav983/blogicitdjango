from django.db import models

# Create your models here.


class Product(models.Model):
    AccountNo = models.CharField(max_length=200, null=False, blank=False,default="")
    AccountType = models.CharField(max_length=200, null=False, blank=False,default="")
    Name = models.CharField(max_length=200, null=False, blank=False,default="")
    PreviousBalance=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    OpenDate=models.CharField(max_length=50, null=False, blank=False,default="")
    Mobile=models.CharField(max_length=50, null=True, blank=False,default="")
    AgentName=models.CharField(max_length=50, null=False, blank=False,default="")
    def __str__(self):
        return self.name
class downloadexcel(models.Model):
    # RecieptNo = models.CharField(max_length=50, null=False, blank=False,default=0)
    AccountNo = models.CharField(max_length=200, null=False, blank=False,default="")
    AccountType = models.CharField(max_length=200, null=False, blank=False,default="")
    Name = models.CharField(max_length=200, null=False, blank=False,default="")
    PreviousBalance=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    OpenDate=models.CharField(max_length=50, null=False, blank=False,default="")
    Mobile=models.CharField(max_length=50, null=True, blank=False,default="")
    AgentName=models.CharField(max_length=50, null=False, blank=False,default="")
    PresentBalance=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    Today=models.CharField(max_length=50, null=False, blank=False,default="")
    Time = models.CharField(max_length=50, null=False, blank=False,default="")
    Recieved=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    id=models.DecimalField(max_digits=10, decimal_places=0,default=0,primary_key=True)
    def __str__(self):
        return self.name

class reporttoday(models.Model):
    AccountNo = models.CharField(max_length=200, null=False, blank=False,default="")
    AccountType = models.CharField(max_length=200, null=False, blank=False,default="")
    Name = models.CharField(max_length=200, null=False, blank=False,default="")
    Recieved=models.DecimalField(max_digits=10, decimal_places=2,default=0)
    OpenDate=models.CharField(max_length=50, null=False, blank=False,default="")
    Mobile=models.CharField(max_length=50, null=True, blank=False,default="")
    AgentName=models.CharField(max_length=50, null=False, blank=False,default="")
    def __str__(self):
        return self.name

class agent(models.Model):
    first_name=models.CharField(max_length=50, null=False, blank=False,default="")
    last_name=models.CharField(max_length=50, null=False, blank=False,default="")
    username=models.CharField(max_length=200, null=False, blank=False,default="")
    email=models.CharField(max_length=200, null=False, blank=False,default="")
    mobile=models.CharField(max_length=50, null=True, blank=False,default="")
    password=models.CharField(max_length=50, null=True, blank=False,default="")
    date_joined=models.CharField(max_length=50, null=True, blank=False,default="")
    is_admin=models.CharField(max_length=50, null=True, blank=False,default="0")
    is_login=models.CharField(max_length=50, null=True, blank=False,default="false")
    is_logout=models.CharField(max_length=50, null=True, blank=False,default="true")
    bank=models.CharField(max_length=100, null=False, blank=False,default="")
    def __str__(self):
        return self.name
class chat(models.Model):
    fname=models.CharField(max_length=50, null=False, blank=False,default="")
    tname=models.CharField(max_length=50, null=False, blank=False,default="")
    msg=models.CharField(max_length=200, null=False, blank=False,default="")
    dt=models.CharField(max_length=50, null=False, blank=False,default="Today")
    def __str__(self):
        return self.name
