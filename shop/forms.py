from django import forms
from . import models

class login1(forms.Form):
    username = forms.CharField(label='Enter your Email', max_length=100)
    password = forms.CharField(label='Enter your Password', max_length=100)



class login(forms.Form):
    username = forms.CharField(label='Enter your Email', max_length=100)
    password = forms.CharField(label='Enter your Password', max_length=100)




class Register_Form(forms.ModelForm):
    class Meta:
        model=models.RegisterModel1
        fields=['First_name','Last_name','email','mobile_no','Addresh','Password1']


class Product_form(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['product_name','category','subcategory','price','desc','pub_date','image']
