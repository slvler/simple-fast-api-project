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
```text
SELECT * FROM pg_type WHERE typname = 'general_status';
CREATE TYPE general_status_enum AS ENUM ('user', 'company');
CREATE TYPE general_status AS ENUM ('user', 'company');
```