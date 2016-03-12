#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "carousel.settings")

    port = os.getenv('PORT', '8000')

    from django.core.management import execute_from_command_line

    args = sys.argv[:]
    args.append(port)
    execute_from_command_line(args)
