from django.db import models

# Create Company api

class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=(('IT','IT'),('NON_IT','NON_IT'),('Mobiles_phones','Mobiles_phones'),))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name +self.location


    #Create model Empoyee

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=(('manager','manager'),('software_devloper','SD'),('project leader','pl'),))
    company=models.ForeignKey(Company,on_delete=models.CASCADE)


    def __str__(self):
        return self.name
    


