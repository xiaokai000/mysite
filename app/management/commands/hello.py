# -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
import os
import logging
import subprocess

INTERPRETER = "/usr/bin/python"


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('hello!')