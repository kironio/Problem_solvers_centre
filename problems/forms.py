from django import forms
from problems.models import Problem, Solution

class ProblemForm(forms.ModelForm):
    
    class Meta:
        model = Problem
        fields = ("title","problem_category","problem_brief","problem_reward","problem_description")

        widgets = {
            'title' : forms.TextInput(attrs= {'class' : 'textinputclass'}),
            'problem_brief': forms.Textarea(attrs= {'class': 'editable medium-editor-textarea postcontent'}),
            'problem_reward': forms.TextInput(attrs= {'class' : 'textinputclass'}),
            'problem_description' : forms.Textarea(attrs= {'class': 'editable medium-editor-textarea postcontent'}), # here postcontent is user created css class
        }


class SolutionForm(forms.ModelForm):
    
    class Meta:
        model = Solution
        fields = ("solution_title","solution_brief")

        widgets = {
            'solution_title' : forms.TextInput(attrs= {'class' : 'textinputclass'}),
            'solution_brief': forms.Textarea(attrs= {'class': 'editable medium-editor-textarea postcontent'}),
        }
