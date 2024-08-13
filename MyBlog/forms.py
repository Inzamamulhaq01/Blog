from django import forms

class Contactform(forms.Form):
    name = forms.CharField(label='name',max_length=30,required=True)
    email = forms.EmailField(label='email',required=True)
    message = forms.CharField(label='message',required=True)

class CommentForm(forms.Form):
    name = forms.CharField(label='name',max_length=30)
    email = forms.EmailField(label='email')
    message = forms.CharField(label='message')
    
