from django.db import models

# Create your models here.
class Quizz(models.Model):
    question = models.CharField(max_length=200, null=True)
    option_1 = models.CharField(max_length=200, null=True)
    option_2 = models.CharField(max_length=200, null=True)
    option_3 = models.CharField(max_length=200, null=True)
    option_4 = models.CharField(max_length=200, null=True)
    option_ok = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.question

