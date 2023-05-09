from django.db import models



class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    totalclasses = models.IntegerField(default=0, null=True, blank=True)
    classesattended = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.title
    