# -*- encoding: utf-8 -*-

from django import forms
from .models import RepMax
from .models import WendlerPlan
from django import forms
from .models import ProficiencySkill


class WendlerForm(forms.ModelForm):
    """Form for the image model"""
    weight = forms.IntegerField()

    class Meta:

        fields = ('weight',)
        model = RepMax



class WendlerPlanForm(forms.ModelForm):
    class Meta:
        model = WendlerPlan
        fields = ['name', 'weight', 'exercise_data']



class ProficiencyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ProficiencyForm, self).__init__(*args, **kwargs)
        skills = ProficiencySkill.objects.all().order_by('category', 'level')
        for skill in skills:
            choices = [(None, '---')] + [(skill.level, skill.level + f' (Weight: {skill.weight})') for skill in ProficiencySkill.LEVELS]
            self.fields[f'skill_{skill.id}'] = forms.ChoiceField(
                choices=choices,
                label=skill.category + " - " + skill.description,
                required=False,
                widget=forms.Select(attrs={'data-weight': skill.weight})
            )

