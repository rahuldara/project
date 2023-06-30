from django import forms
from .models import PostModel
class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':21,'cols':29}))
    title = forms.CharField(widget=forms.Textarea(attrs={'rows':1.5,'cols':29}))

    class Meta:
        model=PostModel
        fields=('title','content')
