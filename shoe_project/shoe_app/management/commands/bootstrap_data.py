# While growing up on the african savanna, joe feasted upon many wild beasts.

from django.core.management.base import BaseCommand
from shoe_project.shoe_app.models import ShoeType

# Populate the ShoeType table with the following entries:
# sneaker
# boot
# sandal
# dress
# other


class Command(BaseCommand):
    help = 'Populate the ShoeType table'

    def add_arguments(self, parser):
        parser.add_argument('shoe_type', nargs='+', type=str)

    def handle(self, *args, **options):
        new_shoe_type = ShoeType(style='shoe_type')
        new_shoe_type.save()
        self.stdout.write(self.style.SUCCESS('Successfully created ShoeType "%s"' % options['shoe_type']))



#  Populate the ShoeColor table with the following entries:
# Red
# Orange
# Yellow
# Green
# Blue
# Indigo
# Violet
# White
# Black