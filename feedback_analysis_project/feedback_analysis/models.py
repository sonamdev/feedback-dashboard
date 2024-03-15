from django.db import models

# Create your models here.
# feedback_analysis/models.py
from django.db import models

class FeedbackReport(models.Model):
    training_rating = models.IntegerField(default=0, help_text="Rating out of 10 for the training")
    trainer_rating = models.IntegerField(default=0, help_text="Rating out of 10 for the trainer")
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback Report {self.id}"
