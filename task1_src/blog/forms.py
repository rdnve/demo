from django import forms

from .models import Feedback


class YearForm(forms.Form):
    year = forms.IntegerField(
        label="Введите год",
        help_text="Для того, чтоб определить, будет ли год високосным или нет.",
        min_value=0,
        max_value=9999,
    )


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ["full_name", "email", "message"]
