
# URL Shortener API

A simple cloud-ready URL Shortener built using FastAPI and Docker with CI/CD using GitHub Actions and deployment on AWS EC2.

---

## Tech Stack

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Docker
- GitHub Actions
- AWS EC2
- Linux

---

## Features

- Create Short URL
- Redirect to Original URL
- List All URLs
- Delete Short URL
- Click Counter

---

## Project Structure

```text
url-shortener-devops/
├── app/
├── tests/
├── scripts/
├── static/
├── templates/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
```

---

## Run Locally

Create Virtual Environment

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

Install Packages

```bash
pip install -r requirements.txt
```

Run

```bash
uvicorn app.main:app --reload
```

Open

```
http://localhost:8000/docs
```

---

## Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up -d
```

---

## Run Tests

```bash
pytest
```

---

## Author

Chinmay Khairnar
