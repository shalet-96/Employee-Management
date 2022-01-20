from django.contrib import auth, messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import EmployeeForm, LeaveRequestForm, loginForm, AssetForm, AssetRequestForm, ClaimRequestForm, \
    TaskSubmissionForm, WorkScheduleForm
from datetime import datetime
# Create your views here.
from .models import LeaveManagement, Employee, AssetManagement, AssetRequest, ClaimManagement, TaskManagement, \
    WorkSchedule


def loginCheck(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username == 'admin':
            print('True')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("/home")
            else:
                return HttpResponse("Invalid Credentials")
        else:
            print('else condition')
            try:
                emp = Employee.objects.get(username=username, password=password)
                print('data', emp.emp_id, emp.username)
                print('XXXX', request.user)
                if emp is not None:
                    if emp.role == 'Manager':
                        return redirect("manager-home", pk=emp.emp_id)
                    elif emp.role == 'HR':
                        return redirect("hr-home", pk=emp.emp_id)
                    else:
                        return redirect("emp-home", pk=emp.emp_id)
                else:
                    messages.info(request, 'invalid credentials')

                    return redirect
            except:
                # messages.info(request, 'invalid credentials')
                return HttpResponse("Invalid Credentials")

    else:
        print('LOGINNNNNNNNNNNNNNNNNNN')
        form = loginForm()
        # context = {
        #     'form': form
        # }
        return render(request, "login.html", {'form': form})


def admin_home(request):
    return render(request, "admin/home.html")


def hr_home(request, pk):
    print("XXXXXXXXX", pk)
    query = Employee.objects.get(emp_id=pk)
    context = {
        'obj': query
    }
    return render(request, "hr-home.html", context=context)


def manager_home(request, pk):
    print("XXXXXXXXX", pk)
    query = Employee.objects.get(emp_id=pk)
    context = {
        'obj': query
    }
    return render(request, "manager-home.html", context=context)


def employee_home(request, pk):
    print("XXXXXXXXX", pk)
    query = Employee.objects.get(emp_id=pk)
    context = {
        'obj': query
    }
    return render(request, "employee/emp-home.html", context=context)


def add_emp(request):
    if request.method == "POST":
        print('ENTER FUNCTION')
        try:
            form = EmployeeForm(request.POST)
            print('XXXX', form.is_valid())
            print('XXXX', form.instance)
            if form.is_valid():
                print('FORM VALID')
                try:
                    form.save()
                    print('form saveD')
                    return redirect("view-emp-list")
                    # return True
                except Exception as e:
                    print('EXCEPYIOn', e)

                    pass
            else:
                print('INVALID')
        except Exception as e:
            print('XXXXXXXXXX', e)

        print('IN TRY')

    else:
        print('else')
        form = EmployeeForm()
    return render(request, "admin/addemp.html", {'form': form})


def view_emp_list(request):
    employees = Employee.objects.all().exclude(username='admin')
    print('aaaaa', employees)
    return render(request, "admin/view-emp-list.html", {'employees': employees})


def delete_emp(request, empid):
    employee = Employee.objects.get(emp_id=empid)
    employee.delete()
    return redirect("/view-emp-list")


# To edit employee details
def edit_emp(request, empid):
    employee = Employee.objects.get(emp_id=empid)
    return render(request, "admin/edit-employee.html", {'employee': employee})


def updateEmp(request, empid):
    employee = Employee.objects.get(emp_id=empid)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/view-emp-list")
    return render(request, "admin/edit-employee.html", {'employee': employee})


def add_asset(request):
    if request.method == "POST":
        print('ENTER FUNCTION')
        try:
            form = AssetForm(request.POST)
            if form.is_valid():
                print('FORM VALID')
                try:
                    form.save()
                    print('form saveD')
                    return redirect("view-asset-list")
                    # return True
                except Exception as e:
                    print('EXCEPTIOn', e)

                    pass
            else:
                print('INVALID')
        except Exception as e:
            print('XXXXXXXXXX', e)

        print('IN TRY')

    else:
        print('else')
        form = AssetForm()
    return render(request, "admin/add-asset.html", {'form': form})


def view_asset_list(request):
    assets = AssetManagement.objects.all()
    return render(request, "admin/view-asset-list.html", {'assets': assets})


def delete_asset(request, pk):
    obj = AssetManagement.objects.get(id=pk)
    obj.delete()
    return redirect("/view-asset-list")


def edit_asset(request, pk):
    obj = AssetManagement.objects.get(id=pk)
    return render(request, "admin/edit-asset.html", {'obj': obj})


def update_asset(request, pk):
    obj = AssetManagement.objects.get(id=pk)
    form = AssetForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("/view-asset-list")
    return render(request, "admin/edit-asset.html", {'obj': obj})


def add_leave_request(request, empid):
    print('PKK', empid)
    query = Employee.objects.get(emp_id=empid)
    print('Query', query)
    if request.method == "POST":
        print('POST')
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            form.instance.emp_id = query
            form.instance.status = 'Pending'
            form.save()
            return redirect("view-leave-request", pk=empid)
    else:
        form = LeaveRequestForm()
        context = {
            'form': form,
            'empid': empid,
            'obj': query,
        }
        return render(request, "employee/request-leave.html", context=context)


def view_leave_request(request, pk):
    obj = Employee.objects.get(emp_id=pk)
    query = LeaveManagement.objects.filter(emp_id__emp_id=pk)
    context = {
        'query': query,
        'obj': obj
    }
    return render(request, "leave/view-leave-request.html", context=context)


def cancel_leave_request(request, empid):
    obj = LeaveManagement.objects.get(id=empid)
    emp_id = obj.emp_id.emp_id
    obj.delete()
    return redirect("view-leave-request", pk=emp_id)


def show(request):
    companies = LeaveManagement.objects.filter(emp_id=request.user)
    return render(request, "show.html", {'companies': companies})


def request_asset(request, empid):
    obj = Employee.objects.get(emp_id=empid)
    if request.method == "POST":
        print('POST')
        form = AssetRequestForm(request.POST)
        if form.is_valid():
            form.instance.emp = obj
            form.instance.status = 'Pending'
            form.save()
            return redirect("view-asset-request", pk=empid)
    else:
        form = AssetRequestForm()
        context = {
            'form': form,
            'empid': empid,
            'obj': obj,
        }
        return render(request, "asset/request-asset.html", context=context)


def view_asset_request(request, pk):
    obj = Employee.objects.get(emp_id=pk)
    query = AssetRequest.objects.filter(emp__emp_id=pk)
    context = {
        'query': query,
        'obj': obj
    }
    return render(request, "asset/view-asset-request.html", context=context)


def cancel_asset_request(request, empid):
    obj = AssetRequest.objects.get(id=empid)
    emp_id = obj.emp.emp_id
    obj.delete()
    return redirect("view-asset-request", pk=emp_id)


def request_claim(request, empid):
    obj = Employee.objects.get(emp_id=empid)
    if request.method == "POST":
        form = ClaimRequestForm(request.POST)
        if form.is_valid():
            form.instance.emp = obj
            form.instance.status = 'Pending'
            form.save()
            return redirect("view-claim-request", pk=empid)
    else:
        form = ClaimRequestForm()
        context = {
            'form': form,
            'empid': empid,
            'obj': obj,
        }
        return render(request, "claim/request-claim.html", context=context)


def view_claim_request(request, pk):
    obj = Employee.objects.get(emp_id=pk)
    query = ClaimManagement.objects.filter(emp__emp_id=pk)
    context = {
        'query': query,
        'obj': obj,
    }
    return render(request, "claim/view-claim-request.html", context=context)


def cancel_claim_request(request, empid):
    obj = ClaimManagement.objects.get(id=empid)
    emp_id = obj.emp.emp_id
    obj.delete()
    return redirect("view-claim-request", pk=emp_id)


def add_task(request, empid):
    print('empid', empid)
    query = Employee.objects.get(emp_id=empid)
    if request.method == "POST":
        form = TaskSubmissionForm(request.POST)
        if form.is_valid():
            form.instance.emp = query
            form.save()
            print('############ form saved')
            return redirect("view-task-list", empid=empid)
    else:
        form = TaskSubmissionForm()
        context = {
            'form': form,
            'empid': empid
        }
        return render(request, "Task/submit-task.html", context=context)


def view_task_list(request, empid):
    print('in view', empid)
    print('task USER', request.user.username)
    query = TaskManagement.objects.filter(emp__emp_id=empid)
    return render(request, "Task/view-task-list.html", {'query': query})


def delete_task(request, empid):
    obj = TaskManagement.objects.get(id=empid)
    empid = obj.emp.emp_id
    obj.delete()
    return redirect("view-task-list", empid=empid)


# To edit employee details
def edit_task(request, empid):
    obj = TaskManagement.objects.get(id=empid)
    return render(request, "Task/edit-task.html", {'obj': obj})


def update_task(request, empid):
    print('UPDATES')
    obj = TaskManagement.objects.get(id=empid)
    query = Employee.objects.get(emp_id=obj.emp.emp_id)
    print('OBJJJJ', obj)
    form = TaskSubmissionForm(request.POST or None, instance=obj)
    print('FORM', form)
    print('form###', form.is_valid())
    if form.is_valid():
        print('TRUE', form.is_valid())
        form.save()
        return redirect("view-task-list", empid=obj.emp.emp_id)
    return render(request, "Task/edit-task.html", {'obj': obj})


def view_task_status(request, pk):
    obj = TaskManagement.objects.get(id=pk)
    return render(request, "Task/view-task-status.html", {'obj': obj})


def submit_task(request, pk):
    obj = TaskManagement.objects.get(id=pk)
    obj.is_submitted = True
    obj.submitted_date = datetime.now()
    obj.save()
    return redirect("view-task-list", empid=obj.emp.emp_id)


def approve_task(request, empid):
    obj = TaskManagement.objects.get(id=empid)
    obj.is_approved = True
    obj.status = 'Approved'
    obj.approved_date = datetime.now()
    obj.save()
    return redirect("/view-submit-task")


def view_submitted_task(request, empid):
    obj = Employee.objects.get(emp_id=empid)
    query = TaskManagement.objects.filter(is_submitted=True)
    context = {
        'query': query,
        'obj': obj,
    }
    return render(request, "Task/view-submitted-tasks.html", context=context)


def reject_task(request, empid):
    obj = TaskManagement.objects.get(id=empid)
    obj.is_approved = False
    obj.status = 'Rejected'
    obj.approved_date = datetime.now()
    obj.save()
    return redirect("/view-submit-task")


def view_emp_leave_request(request, empid):
    obj = Employee.objects.get(emp_id=empid)
    query = LeaveManagement.objects.all()
    context = {
        'query': query,
        'obj': obj,
    }
    return render(request, "leave/view-requests.html", context=context)


def approve_leave(request, empid):
    obj = LeaveManagement.objects.get(id=empid)
    obj.approved_rejected = True
    obj.status = 'Approved'
    obj.save()
    return redirect("/view-requests")


def reject_leave(request, empid):
    obj = LeaveManagement.objects.get(id=empid)
    obj.approved_rejected = False
    obj.status = 'Rejected'
    obj.save()
    return redirect("/view-requests")


def show_asset_request(request, empid):
    obj = Employee.objects.get(emp_id=empid)
    query = AssetRequest.objects.all()
    context = {
        'query': query,
        'obj': obj
    }
    return render(request, "Asset/show-asset-request.html", context=context)


def approve_asset_request(request, empid):
    obj = AssetRequest.objects.get(id=empid)
    obj.status = 'Approved'
    obj.save()
    return redirect("/show-asset-request")


def reject_asset_request(request, empid):
    obj = AssetRequest.objects.get(id=empid)
    obj.status = 'Rejected'
    obj.save()
    return redirect("/show-asset-request")


def show_claim_request(request):
    query = ClaimManagement.objects.all()
    return render(request, "Claim/show-claim-requests.html", {'query': query})


def approve_claim_request(request, empid):
    obj = ClaimManagement.objects.get(id=empid)
    obj.status = 'Approved'
    obj.approved_date = datetime.now()
    obj.save()
    return redirect("/show-claim-request")


def reject_claim_request(request, empid):
    obj = ClaimManagement.objects.get(id=empid)
    obj.status = 'Rejected'
    obj.approved_date = datetime.now()
    obj.save()
    return redirect("/show-claim-request")


def create_schedule(request, empid):
    obj = Employee.objects.get(emp_id=empid)
    if request.method == "POST":
        form = WorkScheduleForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("view-schedule-list")
            except Exception as e:
                pass
    else:
        print('else')
        form = WorkScheduleForm()
        context = {
            'form': form,
            'obj': obj,
        }
    return render(request, "Schedule/create-schedule.html", context=context)


def schedule_list(request, empid):
    obj = Employee.objects.get(emp_id=empid)
    query = WorkSchedule.objects.all()
    context = {
        'query': query,
        'obj': obj,
    }
    return render(request, "Schedule/schedule-list.html", context=context)


def view_schedule(request, empid):
    query = WorkSchedule.objects.filter(emp__emp_id=empid)
    return render(request, "Schedule/view-schedule.html", {'query': query})


def delete_schedule(request, empid):
    obj = WorkSchedule.objects.get(id=empid)
    obj.delete()
    return redirect("view-schedule-list")


def edit_schedule(request, empid):
    print("edit", empid)
    obj = WorkSchedule.objects.get(id=empid)
    form = WorkScheduleForm(request.POST or None, instance=obj)
    return render(request, "Schedule/edit-schedule.html", {'form': form})


def update_schedule(request, empid):
    obj = WorkSchedule.objects.get(id=empid)
    form = WorkScheduleForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect("view-schedule-list")
    return render(request, "Schedule/edit-schedule.html", {'form': form})
