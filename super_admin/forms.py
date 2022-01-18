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
    password = forms.CharField(max_length=100, widget=forms.PasswordInput())

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


class WorkScheduleForm(forms.ModelForm):
    from_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    to_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    emp = forms.ModelChoiceField(queryset=Employee.objects.filter(role='Employee'))

    class Meta:
        model = WorkSchedule
        fields = [
            'emp',
            'from_date',
            'to_date',
            'shift_type',
            'task_info',
            'is_scheduled',
        ]


class AssetForm(forms.ModelForm):
    class Meta:
        model = AssetManagement
        fields = [
            'item',
            'description',
            'no_of_item',
            'is_available'
        ]
    def __init__(self, *args, **kwargs):
        super(AssetForm, self).__init__(*args, **kwargs)

        self.fields['item'].widget.attrs['class'] = 'form-control'
        self.fields['item'].widget.attrs['placeholder'] = 'Item'

        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'

        self.fields['no_of_item'].widget.attrs['class'] = 'form-control'
        self.fields['no_of_item'].widget.attrs['placeholder'] = 'Available quantity'






class LeaveRequestForm(forms.ModelForm):
    from_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    to_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

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
    from_time = forms.TimeField(required=False, widget=forms.widgets.TimeInput(attrs={'type': 'time'}))
    to_time = forms.TimeField(required=False, widget=forms.widgets.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = TaskManagement
        fields = [
            'task',
            'from_time',
            'to_time',
        ]
