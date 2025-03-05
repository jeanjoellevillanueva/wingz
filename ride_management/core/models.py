from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.db import models
from django.db.models import Model
from django.utils import timezone


class User(AbstractUser):
    """
    Object pertaining to the user.
    """
    class Meta:
        db_table = 'USERS'

    ROLE_ADMIN = 'admin'
    ROLE_DRIVER = 'driver'
    ROLE_RIDER = 'rider'
    ROLE_CHOICES = (
        (ROLE_ADMIN, 'Admin'),
        (ROLE_DRIVER, 'Driver'),
        (ROLE_RIDER, 'Rider'),
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ROLE_RIDER
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        default='',
    )

    # Add related_name to prevent conflicts with Django's auth.User model
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions_set', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Ride(Model):
    """
    Object pertaining to the service.
    """
    class Meta:
        db_table = 'RIDES'

    STATUS_ROUTE = 'en-route'
    STATUS_PICKUP = 'pickup'
    STATUS_DROPOFF = 'dropoff'
    STATUS_COMPLETED = 'completed'
    STATUS_CHOICES = (
        (STATUS_ROUTE, 'En Route'),
        (STATUS_PICKUP, 'Pickup'),
        (STATUS_DROPOFF, 'Dropoff'),
        (STATUS_COMPLETED, 'Completed'),
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_ROUTE
    )
    rider = models.ForeignKey(
        User,
        related_name='rides_as_rider',
        on_delete=models.CASCADE
    )
    driver = models.ForeignKey(
        User,
        related_name='rides_as_driver',
        on_delete=models.CASCADE
    )
    pickup_latitude = models.FloatField()
    pickup_longitude = models.FloatField()
    dropoff_latitude = models.FloatField()
    dropoff_longitude = models.FloatField()
    pickup_time = models.DateTimeField()
    
    def get_todays_ride_events(self):
        now = timezone.now()
        return self.rideevents.filter(
            created_at__gte=now - timezone.timedelta(hours=24)
        )


class RideEvent(Model):
    """
    Object pertaining to events that happened
    during the ride/transit.
    """
    class Meta:
        db_table = 'EVENTS'

    ride = models.ForeignKey(
        Ride,
        related_name='rideevents',
        on_delete=models.CASCADE
    )
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id_ride_id} - {self.description}'
