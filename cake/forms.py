from django import forms

class cakeform(forms.Form):
    topping1 = forms.CharField(label="topping1",max_length="200", required=False)
    topping2 = forms.CharField(label="topping2",max_length="200", required=False)
    size=forms.ChoiceField(label="size",choices=[("small","small"),("medium","medium"),("large","large")])


