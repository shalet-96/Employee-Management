from django.contrib import auth, messages
from django.shortcuts import render, redirect
from .forms import EmployeeForm, LeaveRequestForm, loginForm, AssetForm, AssetRequestForm, ClaimRequestForm, \
    TaskSubmissionForm

# Create your views here.
from .models import LeaveManagement, Employee, AssetManagement, AssetRequest, ClaimManagement, TaskManagement


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
                messages.info(request, 'invalid credentials')
                return redirect
        else:
            print('else condition')
            emp = Employee.objects.get(username=username, password=password)
            print('data', emp.emp_id, emp.username)
            print('XXXX', request.user)
            if emp is not None:
                if emp.role == 'Manager':
                    return redirect("manager-home", pk=emp.emp_id)
                elif emp.role == 'HR':
                    return redirect("/hr-home")
                else:
                    return redirect("emp-home", pk=emp.emp_id)
            else:
                messages.info(request, 'invalid credentials')
                return redirect
    else:
        print('LOGINNNNNNNNNNNNNNNNNNN')
        form = loginForm()
        # context = {
        #     'form': form
        # }
        return render(request, "login.html", {'form': form})


def admin_home(request):
    return render(request, "admin/home.html")


def hr_home(request):
    return render(request, "admin/home.html")


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
    form = EmployeeForm(request.POST, instance=employee)
    print('Hello1')
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
                    print('EXCEPYIOn', e)

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
            'empid': empid
        }
        return render(request, "employee/request-leave.html", context=context)


def view_leave_request(request, pk):
    query = LeaveManagement.objects.filter(emp_id__emp_id=pk)
    return render(request, "employee/view-leave-request.html", {'query': query})


# to do:
def cancel_leave_request(request, pk):
    query = LeaveManagement.objects.filter(id=pk)
    query.delete()
    return render(request, "employee/view-leave-request.html", {'query': query})


def show(request):
    companies = LeaveManagement.objects.filter(emp_id=request.user)
    return render(request, "show.html", {'companies': companies})


def request_asset(request, empid):
    query = Employee.objects.get(emp_id=empid)
    print('xxx', query)
    if request.method == "POST":
        print('POST')
        form = AssetRequestForm(request.POST)
        if form.is_valid():
            form.instance.emp = query
            form.instance.status = 'Pending'
            form.save()
            return redirect("view-asset-request", pk=empid)
    else:
        form = AssetRequestForm()
        context = {
            'form': form,
            'empid': empid
        }
        return render(request, "asset/request-asset.html", context=context)


def view_asset_request(request, pk):
    query = AssetRequest.objects.filter(emp__emp_id=pk)
    return render(request, "asset/view-asset-request.html", {'query': query})


# to do
def cancel_asset_request(request, pk):
    query = AssetRequest.objects.filter(id=pk)
    query.delete()
    return render(request, "employee/view-leave-request.html", {'query': query})


def request_claim(request, empid):
    query = Employee.objects.get(emp_id=empid)
    if request.method == "POST":
        form = ClaimRequestForm(request.POST)
        if form.is_valid():
            form.instance.emp = query
            form.instance.status = 'Pending'
            form.save()
            return redirect("view-claim-request", pk=empid)
    else:
        form = ClaimRequestForm()
        context = {
            'form': form,
            'empid': empid
        }
        return render(request, "claim/request-claim.html", context=context)


def view_claim_request(request, pk):
    query = ClaimManagement.objects.filter(emp__emp_id=pk)
    return render(request, "claim/view-claim-request.html", {'query': query})


def submit_task(request, empid):
    query = Employee.objects.get(emp_id=empid)
    if request.method == "POST":
        form = TaskSubmissionForm(request.POST)
        if form.is_valid():
            form.instance.emp = query
            form.instance.is_submitted = True
            form.save()
            return redirect("view-task-list", pk=empid)
    else:
        form = TaskSubmissionForm()
        context = {
            'form': form,
            'empid': empid
        }
        return render(request, "Task/submit-task.html", context=context)


def view_task_list(request, pk):
    query = TaskManagement.objects.filter(emp__emp_id=pk)
    return render(request, "Task/view-task-list.html", {'query': query})


def view_emp_leave_request(request):
    query = LeaveManagement.objects.all()
    return render(request, "leave/view-requests.html", {'query': query})


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


def approve_task(request, empid):
    obj = TaskManagement.objects.get(id=empid)
    obj.is_approved = True
    obj.save()
    return redirect("/view-submit-task")


def view_submitted_task(request):
    query = TaskManagement.objects.filter(is_submitted=True)
    return render(request, "Task/view-submitted-tasks.html", {'query': query})


def reject_task(request, empid):
    obj = TaskManagement.objects.get(id=empid)
    obj.is_approved = False
    obj.save()
    return redirect("/view-submit-task")


def show_asset_request(request):
    query = AssetRequest.objects.all()
    return render(request, "Task/view-submitted-tasks.html", {'query': query})