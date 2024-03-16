from django.db import models
from student.models import Student
# Create your models here.
class Attendancereq(models.Model):
    req_id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()
    request = models.CharField(max_length=45)
    # student_id = models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    file = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'attendancereq'