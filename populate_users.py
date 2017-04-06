import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','nKitchen.settings')

import django
django.setup()

## fake pop script
import random
from users.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
            #fake_name = fakegen.name().split()
            fake_first_name = fakegen.name()
            fake_last_name = fakegen.name()
            fake_email = fakegen.email()

users = User.objects.get_or_create(first_name=fake_first_name,
                                last_name=fake_last_name,
                                email=fake_email)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("Populating complete")
