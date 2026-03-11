from django.db import models
from accounts.models import User
from courses.models import Course

class Booking(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_bookings')
    tutor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tutor_bookings')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
