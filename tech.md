ТЕХНИЧЕСКОЕ ЗАДАНИЕ: E-Shop Стильных Оправ
1. Общие сведения
Цель проекта: Разработка интернет-магазина для продажи одежды. Сайт должен обладать современным пользовательским опытом (SPA-feel) без использования тяжелых JS-фреймворков (React/Vue), полагаясь на HTMX. Язык интерфейса: Английский (English).

2. Стек технологий
Backend: Python / Django.

Database: PostgreSQL.

Frontend:

Стили: Tailwind CSS.

Интерактивность: Alpine.js (для модальных окон и UI-состояний на клиенте).

SPA-поведение: HTMX (AJAX-запросы, частичное обновление DOM, push-url).

Deployment: Docker, Docker Compose, Nginx.

3. Функциональные требования
3.1. Каталог продукции
Отображение списка товаров (одежды) в виде сетки.

Фильтрация: Фильтры по категориям (Men, Women, Material и т.д.) без перезагрузки страницы (HTMX).

Пагинация или "Load More" через HTMX.

3.2. Детальная страница товара
Фотогалерея товара.

Описание, технические характеристики, цена.

Кнопка "Add to Cart": асинхронное добавление с обновлением счетчика корзины.

3.3. Корзина (Shopping Cart)
Реализована в модальном окне (Alpine.js).

Изменение количества и удаление товаров происходит асинхронно.

Динамический пересчет итоговой суммы (HTMX).

3.4. Оформление заказа (Order/Checkout)
Форма создания заказа.

Валидация полей на сервере с возвратом ошибок через HTMX (без перезагрузки).

3.5. Платежная система
Интеграция с NOWPayments (в тексте было noypayment, исправлено согласно контексту "payments" и общеизвестным шлюзам).

Обработка вебхуков для смены статусов заказов.

4. Требования к коду и архитектуре
Парадигма: ООП.

Принципы: DRY (Don't Repeat Yourself), KISS.

Mapping: Использование DTO или ModelForms для маппинга данных где это необходимо.

Безопасность: Защита от стандартных уязвимостей (XSS, CSRF, SQLi) средствами Django.

Best Practices: Fat models / Service layer. Вся бизнес-логика вынесена в слой services.

Комментарии: Запрещены. Код должен быть чистым и самодокументируемым.

5. UI/UX (SPA подход)
Весь фронтенд должен ощущаться как SPA.

Полная перезагрузка страницы только при первом входе.

Все переходы по ссылкам и отправка форм обрабатываются через HTMX (hx-boost, hx-target).

6. Деплой и Окружение
Контейнеризация всех сервисов (Web, DB, Nginx).

nginx раздает статику/медиа и проксирует запросы к gunicorn/uwsgi.

7. Структура проекта
Структура файлов и папок должна строго соответствовать следующей схеме:

Plaintext

eyeframe-shop/
├── docker-compose.yml
├── Dockerfile
├── nginx/
│   └── nginx.conf
├── manage.py
├── config/                 # Django settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── catalog/            # Products, Categories
│   ├── cart/               # Shopping cart
│   ├── orders/             # Order management
│   └── payments/           # NOWPayments integration
├── core/                   # Base classes, mixins, utils
├── services/               # Business logic layer
├── templates/
│   ├── base.html
│   ├── components/         # Reusable HTMX components
│   ├── catalog/
│   ├── cart/
│   └── orders/
├── static/
│   ├── css/
│   └── js/
├── media/                  # User uploaded files
├── requirements.txt
├── .env.example
└── README.md