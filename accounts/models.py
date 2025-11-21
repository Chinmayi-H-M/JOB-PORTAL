from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('employer', 'Employer'),
        ('jobseeker', 'Job Seeker'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.role})"


class EmployerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile')
    company_name = models.CharField(max_length=255)
    website = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.company_name


class JobSeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='jobseeker_profile')
    skills = models.TextField(blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    location = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.user.username

