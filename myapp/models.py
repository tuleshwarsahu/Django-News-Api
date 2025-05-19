from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    basic_salary = models.FloatField(blank=True, null=True)
    hra_enabled = models.BooleanField(default=False)
    hra_amount = models.FloatField(blank=True, null=True)
    gross_salary = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.hra_amount = self.basic_salary * 0.07 if self.hra_enabled else 0.00
        self.gross_salary = self.basic_salary + self.hra_amount
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class Articles(models.Model):
    source = models.CharField(max_length=100, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, null=False, default="Untitled Article")  
    description = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    url_to_image = models.URLField(blank=True, null=True)
    published_at = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Untitled Article"
