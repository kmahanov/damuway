from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    order = models.PositiveIntegerField()

    def __str__(self):
        return self.text

class AnswerOption(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    feedback = models.TextField()

    def __str__(self):
        return self.text

class UserResponse(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(AnswerOption, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)