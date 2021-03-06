from django import forms
from .models import Post

class HomeForm(forms.ModelForm):
	post = forms.CharField(widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Share your thoughts..',}
			)
		)

	class Meta:
		model = Post
		fields = ('post',)