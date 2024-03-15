from django.shortcuts import render

# Create your views here.
# feedback_analysis/views.py
from django.shortcuts import render, redirect
from .forms import FeedbackReportForm
from .ai_module import generate_feedback_report

def submit_feedback(request):
    if request.method == 'POST':
        form = FeedbackReportForm(request.POST)
        if form.is_valid():
            form.save()
            # Generate feedback report
            feedback_report = generate_feedback_report(form.cleaned_data['training_rating'], form.cleaned_data['trainer_rating'])
            return render(request, 'feedback_report.html', {'feedback_report': feedback_report})
    else:
        form = FeedbackReportForm()
    return render(request, 'feedback_submission.html', {'form': form})
