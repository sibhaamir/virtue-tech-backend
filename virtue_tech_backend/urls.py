from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("accounts.urls")),  # your existing auth
    path("api/courses/", include("courses.urls")),
    path("api/payments/", include("payments.urls")),
    path("api/notifications/", include("notifications.urls")),
    path("api/sessions/", include("bookings.urls")),

    # ⭐ ADD THIS NEW LINE FOR STUDENT PANEL BACKEND
    path("api/student/", include("api.urls")),
]
