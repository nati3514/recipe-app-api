"""
Django command to wait for the database to be available.
"""
import time
from psycopg2 import OperationalError as Psycopg2Error  # type: ignore
from django.db.utils import OperationalError  # type: ignore
from django.core.management.base import BaseCommand  # type: ignore

class Command(BaseCommand):
    """Django command to wait for database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):  # at least two spaces before inline comment
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))  # at least two spaces before inline comment
