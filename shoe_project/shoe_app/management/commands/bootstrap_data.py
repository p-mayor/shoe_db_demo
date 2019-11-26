# While growing up on the african savanna, joe feasted upon many wild beasts.

from django.core.management.base import BaseCommand
from shoe_project.shoe_app.models import ShoeType, ShoeColor

# Populate the ShoeType table with the following entries:
# sneaker
# boot
# sandal
# dress
# other

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


class Command(BaseCommand):
    help = 'Populate the ShoeType and ShoeColor tables'

    def handle(self, *args, **options):
        init_shoe_types = ['sneaker', 'boot', 'sandal', 'dress', 'other']
        init_shoe_colors = ['Red', 'Orange', 'Yellow', 'Green',
                            'Blue', 'Indigo', 'Violet', 'White', 'Black']
        for i in init_shoe_types:
            new_shoe_type = ShoeType(style=i)
            new_shoe_type.save()
            self.stdout.write(self.style.SUCCESS('Successfully created ShoeType "%s"' % i))

        for i in init_shoe_colors:
            new_shoe_color = ShoeColor(color_name=i)
            new_shoe_color.save()
            self.stdout.write(self.style.SUCCESS('Successfully created ShoeColor "%s"' % i))
