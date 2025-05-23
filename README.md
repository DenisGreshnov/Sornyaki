# Sornyaki


## Running WebUI
Prepare env
```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
Run
```bash
# dev server
python app.py
# prod server
nohup waitress-serve --host 0.0.0.0 --port 8000 app:app &
# diff? idk
```
