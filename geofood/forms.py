from django import forms

from geofood.models import Post, Restaurant



class PostForm(forms.ModelForm):

    class Meta:
        model= Post
        fields= ('text', 'author')

class RestForm(forms.ModelForm):

    class Meta:
        model= Restaurant
        fields= ('lon', 'lat', 'title', 'category')