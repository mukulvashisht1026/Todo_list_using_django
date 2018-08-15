from django import forms

class Todo_list(forms.Form):
	TASKS = forms.CharField(max_length=50,widget=forms.TextInput(
		attrs={'color':'rgb(255,0,0)','title':'TASKS'}
		))