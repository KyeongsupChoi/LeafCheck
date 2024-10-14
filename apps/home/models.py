# -*- encoding: utf-8 -*-
 

from django.db import models
from django.contrib.auth.models import User

from django.contrib.postgres.fields import JSONField  # If using PostgreSQL

from django.contrib.auth.models import User

from django.db import models


class ProficiencySkill(models.Model):
    LEVELS = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert'),
    ]

    category = models.CharField(max_length=100, help_text="The category of the skill, e.g., Backend Development")
    description = models.TextField(help_text="Description of the skill or proficiency required at this level")
    level = models.CharField(max_length=20, choices=LEVELS, help_text="Proficiency level")
    weight = models.IntegerField(help_text="Weight or score for this level")

    def __str__(self):
        return f'{self.category} - {self.level}'


class WendlerPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wendler_plans')
    name = models.CharField(max_length=100, default='Default Wendler Plan')
    weight = models.FloatField()
    exercise_data = models.JSONField(blank=True, null=True)  # For storing exercise plans as JSON
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

class RepMax(models.Model):
    weight = models.IntegerField(max_length=200)

    def __str__(self):
        return self.title

# Create your models here.

