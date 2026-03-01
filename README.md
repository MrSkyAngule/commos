# Supder

Django REST API проект для приёма и отображения сообщений от устройств.

## Используемые технологии

- Python 3
- Django 6.0.2
- Django REST Framework 3.16.1
- PostgreSQL
- Tkinter
- HTML

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone <url-репозитория>
cd supder
```

### 2. Создать виртуальное окружение и установить зависимости

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Настроить базу данных PostgreSQL

Создать БД и пользователя (настройки в `supder/settings.py`):

```
База:     onigiri
Юзер:     hilok
Пароль:   loki
Хост:     localhost
Порт:     5432
```

```bash
sudo -u postgres psql -c "CREATE USER hilok WITH PASSWORD 'loki';"
sudo -u postgres psql -c "CREATE DATABASE onigiri OWNER hilok;"
```

### 4. Применить миграции

```bash
python manage.py migrate
```

### 5. Запустить сервер

```bash
python manage.py runserver
```

Сервер будет доступен по адресу `http://localhost:8000/`.

### 6. Открыть дашборд

Перейти в браузере на `http://localhost:8000/` — отобразится список всех сообщений.

### 7. Запустить GUI-клиент (опционально)

```bash
python apps.py
```

Откроется Tkinter-окно для отправки POST-запросов на API.
