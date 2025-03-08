from django.db import models
from django.utils import timezone

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('high', '🔥 สูง'),
        ('medium', '⚡ ปานกลาง'),
        ('low', '✅ ต่ำ'),
    ]

    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    due_datetime = models.DateTimeField(null=True, blank=True)  # ✅ เพิ่มวันและเวลาสิ้นสุดของงาน

    def is_due_soon(self):
        if self.due_datetime:
            time_left = self.due_datetime - timezone.now()
            return 0 < time_left.total_seconds() <= 259200  # ✅ แจ้งเตือนหากเหลือ <= 3 วัน (259200 วินาที)
        return False

    def is_overdue(self):
        if self.due_datetime:
            return timezone.now() > self.due_datetime  # ✅ ตรวจสอบว่าหมดเวลาหรือยัง
        return False

    def __str__(self):
        return self.title