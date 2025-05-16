<h1 align="center">🚀 Знакомство с Django</h1>
<p align="center"><a href="https://github.com/SurPetrosian" target="_blank">https://github.com/SurPetrosian</a></p>

---

### 📌 Основной функционал

1. ✅ Инициализирован Django-проект **`config`**.
2. ✅ Настроено виртуальное окружение с помощью **Poetry**.
3. ✅ Создано приложение **`catalog`** и зарегистрировано в `INSTALLED_APPS` конфигурации.
4. ✅ Настроена маршрутизация в файле `config/urls.py`.
5. ✅ Созданы два HTML-шаблона:  
   - 🏠 `home` — домашняя страница  
   - 📞 `contacts` — страница с контактной информацией
6. ✅ Для указанных шаблонов созданы контроллеры (views) и настроены маршруты.

---

<h1 align="center">🗃 Работа с ORM в Django</h1>
<p align="center"><a href="https://github.com/SurPetrosian" target="_blank">https://github.com/SurPetrosian</a></p>

---

### 📌 Основной функционал

1. ✅ Подключена СУБД **PostgreSQL** для работы в проекте.
2. ✅ В приложении `catalog` созданы модели:
   - 📦 `Product`
   - 🗂 `Category`  
   Сформированы миграции и применены к базе данных.
3. ✅ Создан суперпользователь и зарегистрированы модели в **Django Admin**.  
   Настроено отображение в админке для удобства работы.
4. ✅ Через `shell` выполнено:
   - Заполнение категорий
   - Применение произвольных фильтров к объектам моделей
5. ✅ Созданы **фикстуры** для моделей `Product` и `Category`.
6. ✅ Реализована **кастомная команда управления** для добавления тестовых продуктов.


---

### 🔗 Полезные ссылки

- 📘 [Официальная документация Django](https://docs.djangoproject.com/ru/)
- 🐍 [Poetry — Dependency Management for Python](https://python-poetry.org/)
- 🌐 https://github.com/SurPetrosian


---

<h1 align="center">📦 Шаблонизация</h1>
<p align="center"><a href="https://github.com/SurPetrosian" target="_blank">https://github.com/SurPetrosian</a></p>



## Описание

Веб-приложение на **Django**, предназначенное для отображения списка товаров и детальной информации о каждом из них. Проект организован с использованием шаблонов и компонентов, обеспечивающих повторное использование кода и чистую архитектуру. Управление зависимостями осуществляется с помощью **Poetry**.

## Выполненные задачи

### ✅ Задание 1: Страница товара
- Создан контроллер (`products) и шаблон (`products.html`) для отображения полной информации о товаре.
- Отображаются название, описание, изображение и другие характеристики товара.

### ✅ Задание 2: Главная страница
- На главной странице реализован вывод списка товаров с помощью цикла `for` в шаблоне.
- Для компактности описание каждого товара обрезается до первых 100 символов.

### ✅ Задание 3: Базовый шаблон и меню
- Создан **базовый шаблон** (`base.html`) с общими элементами страницы: шапка, подвал, стили.
- Выделен **подшаблоны** (`footer.html`, `header.html`), включаемый в другие шаблоны с помощью `{% include %}`.

---

<h1 align="center">📦 FBV и CBV</h1>
<p align="center"><a href="https://github.com/SurPetrosian" target="_blank">https://github.com/SurPetrosian</a></p>

### ✅ Задание 1: Перевод FBV → CBV

- Все контроллеры, включая **contacts**, переписаны с **Function-Based Views** на **Class-Based Views**.
- Страница **contacts** реализована с использованием **TemplateView**.

### ✅ Задание 2: Реализация блога

- Создано новое приложение *blog*, добавлено в **INSTALLED_APPS**.
- Создана модель Blog со следующими полями:
- - заголовок 
- - содержимое
- - изображение (превью)
- - дата создания
- - признак публикации (is_published)
- - количество просмотров
- Реализован полный CRUD для модели **Blog** с использованием CBV (ListView, DetailView, CreateView, UpdateView, DeleteView).

### ✅ Задание 3: Логика обработки и отображения
- 🔢 При открытии статьи увеличивается счётчик просмотров (number_of_views), реализовано через get_object() в DetailView.
- ✅ В списке блогов отображаются только опубликованные статьи (фильтрация реализована в get_queryset()).
- 🔄 После редактирования статьи происходит перенаправление на страницу просмотра этой статьи (через get_success_url() в UpdateView).
- 📨 Если статья набрала 100 просмотров — автоматически отправляется email-уведомление.

---

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. Установите Poetry (если ещё не установлен):  
   [https://python-poetry.org/docs/#installation](https://python-poetry.org/docs/#installation)

3. Установите зависимости:
   ```bash
   poetry install
   ```

4. Активируйте виртуальное окружение:
   ```bash
   poetry shell
   ```

5. Выполните миграции и запустите сервер:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## Структура проекта
```
project/
│
├── templates/
│   ├── base.html
│   ├── partials/
│   │   └── main_menu.html
│   ├── product_detail.html
│   └── index.html
│
├── static/
│   └── styles.css
│
├── products/
│   ├── views.py
│   ├── models.py
│   └── urls.py
│
├── manage.py
├── pyproject.toml
└── project_name/
    └── settings.py
```

## Технологии

- Язык: **Python**
- Фреймворк: **Django**
- Система шаблонов: **Django Templates**
- Управление зависимостями: **Poetry**
- HTML / CSS (с поддержкой шаблонных тегов Django)


### 🙋‍♂️ Автор

**Suren Petrosian**  
📧 Email: sur141097@gmail.com  
🌐 Сайт: https://github.com/SurPetrosian

---