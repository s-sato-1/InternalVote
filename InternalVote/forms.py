from django import forms

# ====================================================

from .models import Award

# ====================================================

class AwardForm(forms.ModelForm):
    """ AwardForm
    """
    class Meta:
        model = Award
        fields = (
          'award_text',
          'employment_text',
          'prizewinner_text',
          'reason_text',
        )
        widgets = {
          'award_text': forms.Select(attrs={'style': "width: 200px; text-align: center;"}),
          'employment_text': forms.Select(attrs={'style': "width: 200px; text-align: center;"}),
          'prizewinner_text': forms.TextInput(attrs={'style': "width: 200px;"}),
          'reason_text': forms.Textarea(attrs={'cols': 40, 
                                               'row': 4,
                                               'style': "width: 500px; height: 110px;"}),
        }

