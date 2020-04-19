from django import forms
from .models import Content, Comment

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['goods_name','uploader_name', 'price', 'description', ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["user", "text"]