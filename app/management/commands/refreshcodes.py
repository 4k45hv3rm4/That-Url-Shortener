from django.core.management.base import BaseCommand, CommandError
from app.models import ShortURL

class Command(BaseCommand):

    help = 'Refreshes all the shortcode at once'

    def add_arguments(self, parser):
        parser.add_argument('items', type=int)

    def handle(self, *args, **options):
        return ShortURL.objects.refresh_shortcodes(items=options['items'])

