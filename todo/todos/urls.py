from django.urls import path
from django.conf.urls import url
from todos.views import HomeView, ProfileView, AddTaskView, CompleteTaskView
from django.urls import reverse_lazy
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)



urlpatterns = [
        url(r'^$', HomeView.as_view()),
        url(r'^login/$', LoginView.as_view(template_name='index.html')),
        url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('login'))),
        url(r'^profile/$', ProfileView.as_view()),
        url(r'^profile/add-task/$', AddTaskView.as_view()),
        url(r'^profile/complete-task/$', CompleteTaskView.as_view()),
        ]
