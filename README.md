# Acte Normative

People write scrapers for Romanian institutions, send data to this app, we
provide a search interface where they can view a search, follow it and get
emails when new stuff appears.

## Development setup

```bash
pip install -r requirements.txt
echo 'from .settings_base import *' > hub/settings.py
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```
