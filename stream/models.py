from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Stream(models.Model):
    stream_name = models.CharField(max_length=100, unique=True)
    stream_desc = models.TextField(max_length=400)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.stream_name

class Show(models.Model):
    show_name = models.CharField(max_length=100)
    show_desc = models.TextField(max_length=400)
    platform = models.ForeignKey(Stream, on_delete=models.CASCADE, related_name='shows')
    rating = models.PositiveIntegerField(validators = [MaxValueValidator(10), MinValueValidator(1)])
    released = models.BooleanField(default=True)
    released_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"{self.show_name} | {self.rating}"
    

class Review(models.Model):
    comment = models.CharField(max_length=400)
    rating = models.PositiveIntegerField(validators = [MaxValueValidator(10), MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    is_valid_comment = models.BooleanField(default = True)
    shows = models.ForeignKey(Show, on_delete = models.CASCADE, related_name = 'reviews' , null=True)

    def __str__(self):
        return f"{self.shows.show_name} review"
    

