from dj_rest_auth import views as auth_views
from dj_rest_auth.registration import views as reg_views
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from drf_spectacular.utils import extend_schema_view, extend_schema

TAG = "Autenticación"

@extend_schema_view(post=extend_schema(tags=[TAG]))
class LoginView(auth_views.LoginView): pass

@extend_schema_view(post=extend_schema(tags=[TAG]))
class LogoutView(auth_views.LogoutView): pass

@extend_schema_view(post=extend_schema(tags=[TAG]))
class PasswordChangeView(auth_views.PasswordChangeView): pass

@extend_schema_view(post=extend_schema(tags=[TAG]))
class PasswordResetView(auth_views.PasswordResetView): pass

@extend_schema_view(post=extend_schema(tags=[TAG]))
class PasswordResetConfirmView(auth_views.PasswordResetConfirmView): pass

@extend_schema_view(post=extend_schema(tags=[TAG]))
class RegisterView(reg_views.RegisterView): pass

@extend_schema_view(post=extend_schema(tags=[TAG]))
class VerifyEmailView(reg_views.VerifyEmailView): pass

@extend_schema_view(post=extend_schema(tags=[TAG]))
class ResendEmailVerificationView(reg_views.ResendEmailVerificationView): pass

@extend_schema_view(post=extend_schema(tags=[TAG]))
class TokenRefreshView(TokenRefreshView): pass

@extend_schema_view(post=extend_schema(tags=[TAG]))
class TokenVerifyView(TokenVerifyView): pass

@extend_schema_view(
    get=extend_schema(tags=[TAG]),
    put=extend_schema(tags=[TAG]),
    patch=extend_schema(tags=[TAG])
)
class UserDetailsView(auth_views.UserDetailsView): pass
