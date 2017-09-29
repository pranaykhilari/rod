from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()
from rodapp import views
urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r"^accounts/signup/$", views.UserSignup.as_view(), name="account_signup"),
    url(r"^accounts/login/$", views.UserLogin.as_view(), name="account_login"),

    #password reset
    url(r"^accounts/password/reset/$", views.UserPasswordReset.as_view(),name="account_reset_password"),
    url(r"^accounts/password/reset/done/$", views.UserPasswordResetDone.as_view(),name="account_reset_password_done"),
    url(r"^accounts/password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",views.UserPasswordResetKey.as_view(),name="account_reset_password_from_key"),
    url(r"^accounts/password/reset/key/done/$", views.UserPasswordResetKeyDone.as_view(),name="account_reset_password_from_key_done"),
    url(r"^accounts/profile/$", views.dashboard),
    url(r"^$",views.is_user_authenticated),
    url(r"^userlogin/$",views.user_logout),
    url(r'^accounts/', include('allauth.urls')),
]
