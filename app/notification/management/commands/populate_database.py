from django.core.management.base import BaseCommand

from notification.models import NotificationType, Rule


class Command(BaseCommand):
    help = "Populate the database with initial data"

    def handle(self, *args, **options):
        notification_types = {
            "news": {
                "time_window": 100,
                "repetitions": 10,
            },
            "marketing": {
                "time_window": 100,
                "repetitions": 10,
            },
            "update": {
                "time_window": 100,
                "repetitions": 10,
            },
        }

        for notification_type_name in notification_types.keys():
            notification_type, _ = NotificationType.objects.get_or_create(
                name=notification_type_name
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully created notification type {notification_type_name}"
                )
            )
            Rule.objects.update_or_create(
                notification_type=notification_type,
                defaults={
                    "time_window": notification_types[notification_type_name][
                        "time_window"
                    ],
                    "repetitions": notification_types[notification_type_name][
                        "repetitions"
                    ],
                },
            )
            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully created rule for notification {notification_type_name}"
                )
            )
