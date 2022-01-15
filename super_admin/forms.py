from calendar import calendar

from django import forms
from .models import *


# This is for employee

class loginForm(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())

    def __init__(self, *args, **kwargs):
        super(loginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'username',
            'password',
            'first_name',
            'last_name',
            'department',
            'role',
            'email',
            'phone'
        ]

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['department'].widget.attrs['class'] = 'form-control'
        self.fields['department'].widget.attrs['placeholder'] = 'Department'
        self.fields['role'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone'


class AssetForm(forms.ModelForm):
    class Meta:
        model = AssetManagement
        fields = [
            'item',
            'description',
            'no_of_item',
            'is_available'
        ]


class LeaveRequestForm(forms.ModelForm):
    class Meta:
        model = LeaveManagement
        fields = [
            'from_date',
            'to_date',
            'reason'
        ]


class AssetRequestForm(forms.ModelForm):
    class Meta:
        model = AssetRequest
        fields = [
            'item',
            'purpose'
        ]


class ClaimRequestForm(forms.ModelForm):
    class Meta:
        model = ClaimManagement
        fields = [
            'claim_type',
            'claim_name',
            'amount',
        ]


class TaskSubmissionForm(forms.ModelForm):
    class Meta:
        model = TaskManagement
        fields = [
            'task',
            'from_time',
            'to_time',
        ]
