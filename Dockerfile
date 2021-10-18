FROM python:3.9.5-alpine

WORKDIR /usr/src/app

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1

# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

COPY . .

RUN apk update \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && sed -i 's/\r$//g' /usr/src/app/entrypoint.sh \
    && chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]