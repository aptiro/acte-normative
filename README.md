## Development setup

```bash
pip install -r requirements.txt
echo 'from .settings_base import *' > hub/settings.py
./manage.py migrate
./manage.py runserver
```
