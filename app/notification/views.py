import logging
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from notification.exceptions import NotificationServiceError, RateLimitExceeded
from .forms import NotificationForm
from .services.notifications import NotificationService
from notification.gateway.gateway import Gateway

logger = logging.getLogger(__name__)


class SolutionView(View):
    def get(self, request, *args, **kwargs):
        form = NotificationForm()
        return render(request, "notification/solution.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = NotificationForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data["user"]
            message = form.cleaned_data["message"]
            notification_type = form.cleaned_data["notification_type"]
            try:
                NotificationService(gateway=Gateway()).send(
                    type=notification_type, user_id=user, message=message
                )
            except NotificationServiceError as exc:
                logger.error("Notification service failed", exc_info=exc)
                form.add_error(None, exc.message)
                return render(request, "notification/solution.html", {"form": form})
            except Exception as exc:
                logger.error("An unexpected error occurred", exc_info=exc)
                form.add_error(None, "An unexpected error occurred")
                return render(request, "notification/solution.html", {"form": form})
            return redirect(reverse("solution"))
        return render(request, "notification/solution.html", {"form": form})
