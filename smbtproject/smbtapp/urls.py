
from django.contrib import admin
from django.urls import path

from smbtapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index_page'),
    path('login', views.login, name='login'),
    path('unit_master',views.unit_master,name='unit_master'),
    path('cluster_master',views.cluster_master,name='cluster_master'),
    path('user_master',views.user_master,name='user_master'),
    path('state_master', views.state_master, name='state_master'),
    path('country_master', views.country_master, name='country_master'),
    path('role_master', views.role_master, name='role_master'),
    path('revenue_targets',views.revenue_targets,name='revenue_targets'),
    path('admission_targets', views.admission_targets, name='admission_targets'),
    path('report_calls',views.report_calls,name='report_calls'),
    path('report_activity',views.report_activity,name='report_activity'),
    path('masterlist',views.masterlist,name='masterlist'),


]
