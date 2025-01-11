```text
python -m venv venv
source venv/bin/activate
uvicorn main:app --reload
```
```text
alembic revision -m "bla bla bla"
alembic upgrade head
alembic downgrade -1
```