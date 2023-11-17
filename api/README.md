# Velvet API

### Setup

**Create a virtual environment**

```bash
python -m venv env
```

**Activate the environment**

```bash
env\Scripts\activate.bat
```

**Install all dependencies**

```bash
pip install -r requirements.txt
```

<br/>

### Docker

To start the database

```bash
docker compose -f docker-compose.dev.yaml --env-file .env.docker-compose up -d
```

<br/>

To stop the database

```bash
docker compose -f docker-compose.dev.yaml --env-file .env.docker-compose down
```
