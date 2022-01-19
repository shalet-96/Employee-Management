"""management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from super_admin import views as views_a

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login-a', views_a.loginCheck, name="login-a"),
    #admin
    path('home', views_a.admin_home, name="home"),
    path('add_emp', views_a.add_emp),
    path('view-emp-list', views_a.view_emp_list, name="view-emp-list"),
    path('delete-emp/<str:empid>', views_a.delete_emp),
    path('edit-emp/<str:empid>', views_a.edit_emp),
    path('update-emp/<str:empid>', views_a.updateEmp),
    path('add-asset', views_a.add_asset),
    path('view-asset-list', views_a.view_asset_list, name="view-asset-list"),
    path('delete-asset/<str:pk>', views_a.delete_asset),
    path('edit-asset/<str:pk>', views_a.edit_asset),
    path('update-asset/<str:pk>', views_a.update_asset),
    # manager
    path(r'manager-home/(?P<pk>\d+)/$', views_a.manager_home, name="manager-home"),
    path('view-requests/<str:empid>', views_a.view_emp_leave_request, name='view-requests'),
    path('approve-leave/<str:empid>', views_a.approve_leave),
    path('reject-leave/<str:empid>', views_a.reject_leave),

    path('view-submit-task/<str:empid>', views_a.view_submitted_task, name='view-submit-task'),
    path('approve-task/<str:empid>', views_a.approve_task),
    path('reject-task/<str:empid>', views_a.reject_task),

    path('show-asset-request/<str:empid>', views_a.show_asset_request, name='show-asset-request'),
    path('approve-asset-request/<str:empid>', views_a.approve_asset_request),
    path('reject-asset-request/<str:empid>', views_a.reject_asset_request),

    path('show-claim-request', views_a.show_claim_request, name='show-claim-request'),
    path('approve-claim-request/<str:empid>', views_a.approve_claim_request),
    path('reject-claim-request/<str:empid>', views_a.reject_claim_request),
    #HR
    path(r'hr-home/(?P<pk>\d+)/$', views_a.hr_home, name="hr-home"),

    # employee
    path(r'emp-home/(?P<pk>\d+)/$', views_a.employee_home, name="emp-home"),
    path(r'view-leave-request/(?P<pk>\d+)/$', views_a.view_leave_request, name='view-leave-request'),
    path('request-leave/<str:empid>', views_a.add_leave_request, name='request-leave'),
    path('cancel-leave/<str:empid>', views_a.cancel_leave_request),

    path('request-asset/<str:empid>', views_a.request_asset, name='request-asset'),
    path(r'view-asset-request/(?P<pk>\d+)/$', views_a.view_asset_request, name='view-asset-request'),
    path('cancel-asset/<str:empid>', views_a.cancel_asset_request),

    path('request-claim/<str:empid>', views_a.request_claim, name='request-claim'),
    path(r'view-claim-request/(?P<pk>\d+)/$', views_a.view_claim_request, name='view-claim-request'),
    path('cancel-claim/<str:empid>', views_a.cancel_claim_request),

    # TASK
    path('view-task-list/<str:empid>', views_a.view_task_list, name='view-task-list'),
    path('create-task/<str:empid>', views_a.add_task, name='create-task'),
    path('submit-task/<str:pk>', views_a.submit_task),
    path('view-task-status/<str:pk>', views_a.view_task_status),
    path('delete-task/<str:empid>', views_a.delete_task),
    path('edit-task/<str:empid>', views_a.edit_task),
    path('update-task/<str:empid>', views_a.update_task),

    #Schedule
    path('create-schedule/<str:empid>', views_a.create_schedule, name='create-schedule'),
    path('view-schedule-list/<str:empid>', views_a.schedule_list, name="view-schedule-list"),
    path('view-schedule/<str:empid>', views_a.view_schedule, name='view-schedule'),
    path('delete-schedule/<str:empid>', views_a.delete_schedule),
    path('edit-schedule/<str:empid>', views_a.edit_schedule),
    path('update-schedule/<str:empid>', views_a.update_schedule),

    # Homepage path
    path('', TemplateView.as_view(template_name='admin/home.html'), name='home'),

    # inbuilt login path
    path('accounts/', include('django.contrib.auth.urls')),
]
# for Media Storage
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
