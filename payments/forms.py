from django import forms

class MakePayment(forms.Form):
    MONTH_CHOICES = [(i,i,) for i in xrange(1,12)]
    YEARS_CHOICES = [(i,i,) for i in xrange(2016,2036)]

    name = forms.CharField(max_length=20, label='Name')
    surname = forms.CharField(max_length=20, label='Surname')
    Address = forms.CharField(max_length=100, label='Address')
    City = forms.CharField(max_length=100, label='City')
    Poscode = forms.IntegerField(label='Postcode')
    credit_card = forms.IntegerField(label='Credit card number')
    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES)
    expiry_year = forms.ChoiceField(label='Year', choices=YEARS_CHOICES)
    cvv = forms.IntegerField(label='CVV')
    stripe_id = forms.CharField(widget=forms.HiddenInput)

