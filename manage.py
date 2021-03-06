#!/usr/bin/env python
"""
Manage the djangoapp
"""
import os
import sys

from django.core.management import execute_from_command_line

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sql_grader.settings')
    execute_from_command_line(sys.argv)
