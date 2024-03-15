# feedback_analysis/forms.py
from django import forms
from .models import FeedbackReport

class FeedbackReportForm(forms.ModelForm):
    class Meta:
        model = FeedbackReport
        fields = ['training_rating', 'trainer_rating']
