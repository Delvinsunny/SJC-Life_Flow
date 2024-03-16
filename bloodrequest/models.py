from django.db import models
from patient.models import Patient
# Create your models here.
class Bloodrequest(models.Model):
    blood_id = models.AutoField(primary_key=True)
    # patient_id = models.IntegerField()
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    group = models.CharField(max_length=45)      
    unit = models.CharField(max_length=45)       
    hospital = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=45)
    document = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'bloodrequest'