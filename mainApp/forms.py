from django import forms
from django.contrib.auth import get_user_model

User = get_user_model() 

class CommentForm(forms.Form):
	
	comment = forms.CharField(widget = forms.Textarea)

class RegisrationForm(forms.ModelForm): 

	password = forms.CharField(widget = forms.PasswordInput)
	password_check = forms.CharField(widget = forms.PasswordInput)

	class Meta:

		model = User
		fields = ['username', 'password', 'password_check', 'first_name', 'last_name', 'email']

	
	def __init__(self, *args, **kwargs):
		super(RegisrationForm, self).__init__(*args, **kwargs)
		#self.fields['username'].label = 'пользовательский ник' #Overloaded and make labels with another language
		self.fields['username'].help_text = 'Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'

	def clean(self):
		username = self.cleaned_data['username']
		password = self.cleaned_data['password']
		password_check = self.cleaned_data['password_check']

		if User.objects.filter(username = username).exists():
			raise forms.ValidationError('User with that username already exists')

		if password != password_check:
			raise forms.ValidationError('Passwords dont equal')

	