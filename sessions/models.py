from django.db import models
from accounts.models import User
from courses.models import Course

class Session(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutor_sessions')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_sessions')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    status = models.CharField(max_length=20, choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='scheduled')

    def __str__(self):
        return f"{self.course.title} - {self.tutor.username} - {self.student.username}"
