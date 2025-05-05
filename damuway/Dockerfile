FROM python:3.11-slim


RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app


COPY . /app/


RUN pip install --upgrade pip


RUN pip install -r requirements.txt


RUN pip install torch==2.2.2+cpu --extra-index-url https://download.pytorch.org/whl/cpu


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
