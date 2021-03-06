#!/usr/bin/env python
import os
import sys
import warnings

import dotenv

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    dotenv.read_dotenv()

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "opencanada.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
