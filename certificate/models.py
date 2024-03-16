from django.db import models
from student.models import Student
# Create your models here.
class Certificate(models.Model):
    certificate_id = models.AutoField(primary_key=True)
    # student_id = models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    donated_date = models.DateField()
    certificate = models.CharField(max_length=500)
    hospital = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'certificate'