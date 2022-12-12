from django.core.management import BaseCommand

from geoservice.core.parse import parse_city


class Command(BaseCommand):
    """Команда для запуска пулинга телеграм бота."""

    help = "Запуск парсинга csv файла"  # noqa

    def handle(self, *args, **options):
        """Запуск парсинга."""
        parse_city()
