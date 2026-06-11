from django.db import models
from users.models import User


class Subject(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subjects"
    )

    subject_name = models.CharField(max_length=100)
    professor_name = models.CharField(max_length=100)

    credits = models.IntegerField(default=3)
    threshold = models.IntegerField(default=75)
    classes_per_week = models.IntegerField(default=3)

    def __str__(self):
        return self.subject_name