import os

GOOD = os.environ.get("GOOD_HASH")
BAD = os.environ.get("BAD_HASH")

os.system(f"git bisect start {BAD} {GOOD}")
os.system("git bisect run .venv3.9/bin/python manage.py test")