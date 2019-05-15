from django.db import models

# Create your models here.


class Lesson(models.Model):
    name = models.CharField(max_length=200)
    file_question = models.FileField(upload_to='question', null=True)
    file_answers = models.FileField(upload_to='answers', null=True)

    def __str__(self):
        return self.name
