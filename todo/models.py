from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=200) #ชื่องาน
    completed = models.BooleanField(default=False) #สถานะงาน
    created_at = models.DateTimeField(auto_now_add=True) #วันที่สร้างงาน

    def __str__(self):
        return self.title