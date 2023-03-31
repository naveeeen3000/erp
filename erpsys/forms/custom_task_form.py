from django import forms



class CustomTaskForm(forms.Form):
    item_ids = forms.FileField()