from calendar import calendar

from django import forms
from .models import *


# This is for employee

class loginForm(forms.Form):
    username = forms.CharField(max_length=250)
    password = forms.CharField(max_length=100)


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