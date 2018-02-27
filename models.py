# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class ActiveAndDateCreated(models.Model):
    class Meta:
        abstract = True

    date_created = models.DateTimeField(default=timezone.now, editable=False)
    is_active = models.BooleanField(default=True)

class Entity(ActiveAndDateCreated):
    class Meta:
        abstract = True

    name = models.CharField(max_length=50, unique=True)

class NeoAgent(ActiveAndDateCreated):
    # A supervisor is an agent assigned to a zone
    # Assign an agent to an area, supervisors to a zone
    # Ensure an agent cannot have both area and zone set.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        abstract = True

    def get_full_name(self):
        return '%s %s' % (self.first_name.title(), self.last_name.title())

class NeoPhoneNumber(models.Model):
    number = models.CharField(max_length=10, unique=True)

    class Meta:
        abstract = True

    def __str__(self):
        return '%s - %s' % (self.agent.get_full_name(), self.number)