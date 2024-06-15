from django.db import models # type: ignore

# Create your models here.



class Company(models.Model):
    company_name = models.CharField(max_length=50,null=False)
    email = models.EmailField(null=False, unique=True)
    company_code = models.CharField(max_length=50,unique=True,null=True)
    strength = models.IntegerField(default=0,null=True)
    web_site = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)


    def __str_(self):
        return self.company_name