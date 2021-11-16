from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class CompletePayment(models.Model):
    member_id = models.AutoField(primary_key=True)
    FullName=models.CharField(max_length=500)
    Emailaddress=models.EmailField()
    Age=models.IntegerField(validators=[MaxValueValidator(65), MinValueValidator(18)])
    batch=models.IntegerField()
    payment=models.IntegerField()

    def __str__(self):
        return self.FullName