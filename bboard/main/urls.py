from django.urls import path

from .views import BBLogoutView, ProfileEditView, BbLoginView, other_page, profile, index, PasswordEditView

app_name = 'main'
urlpatterns = [
    path('account/logout/', BBLogoutView.as_view(), name='logout'),
    path('accounts/password/edit/', PasswordEditView.as_view(), name='password_edit'),
    path('accounts/profile/edit/', ProfileEditView.as_view(), name='profile-edit'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/login/', BbLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
