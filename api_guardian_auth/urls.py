from django.urls import path
from .schema import (
    LoginView, LogoutView, PasswordChangeView, PasswordResetView,
    PasswordResetConfirmView, RegisterView, VerifyEmailView,
    ResendEmailVerificationView, TokenVerifyView, TokenRefreshView,
    UserDetailsView
)

urlpatterns = [
    # Autenticación básica
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("password/change/", PasswordChangeView.as_view(), name="rest_password_change"),
    path("password/reset/", PasswordResetView.as_view(), name="rest_password_reset"),
    path("password/reset/confirm/", PasswordResetConfirmView.as_view(), name="rest_password_reset_confirm"),

    # Registro y verificación
    path("registration/", RegisterView.as_view(), name="rest_register"),
    path("registration/verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"),
    path("registration/resend-email/", ResendEmailVerificationView.as_view(), name="rest_resend_email"),

    # JWT (si usas JWT)
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # Usuario autenticado
    path("user/", UserDetailsView.as_view(), name="rest_user_details"),
]
