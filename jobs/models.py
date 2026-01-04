from django.db import models
from accounts.models import User

class Job(models.Model):
    employer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'employer'}
    )
    title = models.CharField(max_length=200)
    description = models.TextField()
    requirements = models.TextField()
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    deadline = models.DateField()
    is_filled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'jobseeker'}
    )
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Applied')

    def __str__(self):
        return f"{self.applicant.username} → {self.job.title}"

