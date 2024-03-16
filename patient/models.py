from django.db import models

# Create your models here.
class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(max_length=45)
    age = models.IntegerField()
    date = models.DateField()
    bloodgroup = models.CharField(max_length=45)
    bystandername = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    status = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'patient'