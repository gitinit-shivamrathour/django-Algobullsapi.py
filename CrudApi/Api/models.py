from datetime import date
from django.db import models
from django.forms import ValidationError


class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    tags = models.TextField(null=True)
    status = models.CharField(max_length=100, default="OPEN")

    # function to split tags
    def tag_list(self):
        taglist = self.tags.split(',')
        return taglist

    # logic for due_date
    def clean(self):
        super().clean()

        if self.due_date < date.today():
            raise ValidationError("Incorrect due date")
