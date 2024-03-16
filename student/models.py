from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    adm_no = models.CharField(max_length=45)
    course = models.CharField(max_length=45)
    year = models.CharField(max_length=45)
    dob = models.CharField(max_length=45)
    phone = models.CharField(max_length=45)
    bloodgroup = models.CharField(max_length=45)
    photo = models.CharField(max_length=300)
    status = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'student'