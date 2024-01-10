from django.db import models

# Create your models here.
class MyModel(models.Model):
    roll = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    birthday = models.DateField()
    age = models.IntegerField()
    cgpa = models.FloatField()
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    reservation_time = models.DateTimeField()
    time_field = models.TimeField()
    decimal_field = models.DecimalField(max_digits=19, decimal_places=10, blank = True, null =True)
    duration_field = models.DurationField()
    file = models.FileField(upload_to='files/')
    slug_field = models.SlugField()
    text = models.TextField()
    
    def __str__(self):
        return f'roll : {self.roll} - {self.name}'