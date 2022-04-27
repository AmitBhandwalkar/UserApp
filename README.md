# userapp
userapp it's is a django app he can used with multiple projects



How Use User app

step1) add userapp folder in project

step2) add userapp in settings.py file installed app list
->INSTALLED_APPS = [
    'userapp',
]

step3)include userapp path in urls.py file
->urlpatterns = [
    path('user/', include('user.urls')),
]


