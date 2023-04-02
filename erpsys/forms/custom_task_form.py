from django import forms



class CustomTaskForm(forms.Form):
    authorization_key = forms.CharField(widget=forms.Textarea)
    item_ids = forms.CharField(widget=forms.Textarea)