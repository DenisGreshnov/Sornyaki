# Sornyaki


## Running WebUI
Prepare env
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Run
```bash
# dev server
python app.py
# prod server
waitress-serve --host 127.0.0.1 --port 8000 app:app
# diff? idk
```
