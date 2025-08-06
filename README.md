📚 Django Quotes Project
Цей проєкт — це вебзастосунок на Django, який дозволяє переглядати, додавати та керувати цитатами та авторами.
🔧 Технології
Python 3.11

Django 4.x

SQLite (або PostgreSQL)

HTML/CSS (шаблони Django)

Font Awesome (для іконок в адмінці)
🗂️ Структура
DjangoProject-main/
├── hw10_django/
│   └── hw_project/
│       ├── manage.py
│       ├── hw_project/        # Головна конфігурація Django
│       └── quotes/            # Основний застосунок
│           ├── models.py
│           ├── forms.py
│           ├── views.py
│           └── ...
├── static/                    # Статичні файли для адмінки
├── postgres.py                # Альтернативне підключення до PostgreSQL
⚙️ Встановлення
Клонувати репозиторій:
git clone https://github.com/your-username/DjangoProject-main.git
cd DjangoProject-main/hw10_django/hw_project
Створити та активувати віртуальне середовище:
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Встановити залежності:

pip install -r requirements.txt
Якщо файл requirements.txt відсутній, створіть його командою: pip freeze > requirements.txt
Міграції та запуск:python manage.py migrate
python manage.py runserver
Адміністрування (створення суперкористувача):python manage.py createsuperuser
✅ Основні можливості
Додавання/редагування цитат та авторів

Перегляд списку цитат

Пошук за автором або тегами

Інтеграція з базою даних MongoDB (опційно)

Статичні файли та кастомізація адмінки
🗃️ Робота з PostgreSQL
У файлі postgres.py знаходиться приклад підключення до PostgreSQL. Перед використанням змініть налаштування доступу:DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

