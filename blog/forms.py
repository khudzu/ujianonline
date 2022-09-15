from django import forms


class PostForm(forms.Form):
	nama		= forms.CharField(max_length = 20)
	alamat		= forms.CharField(
		widget = forms.Textarea
		)
	nik	= forms.CharField(max_length = 20)