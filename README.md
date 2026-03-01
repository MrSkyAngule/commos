# Supder

Django REST API проект для приёма и отображения сообщений от устройств.

## Стек

- Python 3
- Django 6.0.2
- Django REST Framework 3.16.1
- PostgreSQL
- Tkinter (GUI-клиент)

## Структура проекта

```
supder/          — настройки Django-проекта
commo/           — модель Commo (device_id, data, created_at)
apis/            — REST API (ViewSet + Serializer)
web_apps/        — веб-интерфейс (дашборд)
templates/       — HTML-шаблоны
apps.py          — GUI-клиент для отправки данных через POST
```

## API эндпоинты

| Метод    | URL                      | Описание              |
|----------|--------------------------|-----------------------|
| GET      | `/api/api/messages/`     | Список всех сообщений |
| POST     | `/api/api/messages/`     | Создать сообщение     |
| GET      | `/api/api/messages/{id}/`| Получить по ID        |
| PUT      | `/api/api/messages/{id}/`| Обновить              |
| DELETE   | `/api/api/messages/{id}/`| Удалить               |

Формат тела POST-запроса:
```json
{
  "device_id": "device_001",
  "data": "36.6"
}
```

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
