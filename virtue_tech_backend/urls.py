from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "Virtue Tech Backend Running 🚀"
    })


urlpatterns = [
    path("", home),   # root route

    path("admin/", admin.site.urls),

    path("auth/", include("accounts.urls")),

    path("api/courses/", include("courses.urls")),
    path("api/payments/", include("payments.urls")),
    path("api/notifications/", include("notifications.urls")),
    path("api/sessions/", include("bookings.urls")),

    path("api/student/", include("api.urls")),
]