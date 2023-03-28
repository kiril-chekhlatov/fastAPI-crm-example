# FastAPI - Test CRM for universities

A small CRM system for universities is made for a real business task. 
There are pytest tests, FactoryBoy.
The project uses CRUD with Pydantic, SqlAlchemy and Alembic.
JWT authorization is used. API documentation is available in Swagger

Endpoint map with documentation for 127.0.0.1 (standard host + port):
- Swagger <a href="http://127.0.0.1:8000/docs">http://127.0.0.1:8000/docs


# Launch project on Ubuntu with python3.8.10 and PostgreSQL 12.14:
1. `git clone <project_url>`
2. `cd <project_name>`
3. `python3 -m venv venv`
4. `. venv/bin/activate`
5. `pip3 install -r requirements.txt`
6. `cd app`
7. `python3 backend_pre_start.py`
8. `alembic upgrade head`
9. `python3 initial_data.py`
10. `uvicorn main:app --reload`

# Launch tests on Ubuntu with python3.8.10 and PostgreSQL 12.14: 
1. `git clone <project_url>`
2. `cd <project_name>`
3. `python3 -m venv venv`
4. `. venv/bin/activate`
5. `pip3 install -r requirements.txt`
6. `cd app`
7. `python3 backend_pre_start.py`
8. `alembic upgrade head`
9. `python3 initial_data.py`
10. `python3 -m pytest tests`
