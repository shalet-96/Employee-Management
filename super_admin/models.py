from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = (
    ("Manager", "Manager"),
    ("HR", "HR"),
    ("Employee", "Employee"),
)
CLAIM_TYPE = (
    ("Internet", "Internet"),
    ("Travel", "Travel"),
    ("Medical", "Medical"),
)
STATUS = (
    ("Approved", "Approved"),
    ("Rejected", "Rejected"),
    ("Pending", "Pending"),
)


# Create your models here.
class Employee(AbstractUser):
    username = models.CharField(max_length=250, unique=True)
    password = models.CharField(max_length=250)
    emp_id = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        print('saveeeeeeeeeee')
        if self.emp_id == None:
            self.emp_id = uuid.uuid4()
        super(Employee, self).save(*args, **kwargs)

    class Meta:
        db_table = "employee_1"


class LeaveManagement(models.Model):
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    from_date = models.DateField()
    to_date = models.DateField()
    reason = models.CharField(max_length=100)
    approved_rejected = models.BooleanField(default=False)
    status = models.CharField(max_length=100, null=True, blank=True)
    approved_date = models.DateTimeField(null=True, blank=True)
    rejection_reason = models.CharField(max_length=100, null=True, blank=True)


class AssetManagement(models.Model):
    item = models.CharField(max_length=100)
    item_code = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=250, blank=True, null=True)
    no_of_item = models.IntegerField(default=0)
    is_available = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.item_code == None:
            self.item_code = uuid.uuid4()
        super(AssetManagement, self).save(*args, **kwargs)

    def __str__(self):
        return self.item


class AssetRequest(models.Model):
    item = models.ForeignKey(AssetManagement, on_delete=models.CASCADE)
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=250)
    status = models.CharField(max_length=100, null=True, blank=True)
    request_date = models.DateTimeField(auto_now_add=True)


class ClaimManagement(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    claim_id = models.CharField(max_length=100, blank=True, null=True)
    claim_type = models.CharField(max_length=50, choices=CLAIM_TYPE)
    claim_name = models.CharField(max_length=250, blank=True, null=True)
    amount = models.FloatField()
    status = models.CharField(max_length=100, null=True, blank=True)
    request_date = models.DateTimeField(auto_now_add=True)
    approved_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.claim_id == None:
            self.claim_id = uuid.uuid4()
        super(ClaimManagement, self).save(*args, **kwargs)


class TaskManagement(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    task = models.CharField(max_length=250)
    from_time = models.DateTimeField(null=True, blank=True)
    to_time = models.DateTimeField(null=True, blank=True)
    is_submitted = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)
    submitted_date = models.DateTimeField(auto_now_add=True)
    approved_date = models.DateTimeField(null=True, blank=True)
