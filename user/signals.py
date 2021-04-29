
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from store.models import Customer

def create_customer(sender,instance,created,**kwargs):
    if created:
        name = instance.first_name + '  ' + instance.last_name
        customer = Customer(name=name, email=instance.email, user_id=instance.id)  # or user=instance
        customer.save()

    # print(sender)
    # print(instance)
    # print(created)
    # print(f'{kwargs}')

post_save.connect(create_customer, sender=User)
