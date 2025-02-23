## Install the package
```bash
pip install -r requirements.txt
``` 

## update the package
```bash
pip freeze > requirements.txt
``` 

## start development server
```bash
uvicorn app.main:app --reload
fastapi dev main.py --reload
```

