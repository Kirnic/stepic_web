from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateField(null=True)
    rating = models.IntegerField(null=True)
    author = models.CharField(max_length=50)
    likes = models.ManyToManyField(User)
    objects = models.Manager()
    manager = QuestionManager()


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(null=True)
    question = models.ForeignKey(Question)
    author = models.ForeignKey(User)


