
# Документация API для Блога

## Общее описание API
Этот API позволяет пользователям взаимодействовать с ресурсами блога, такими как посты и комментарии. Доступ к некоторым операциям (создание, редактирование и удаление постов и комментариев) требует аутентификации.

## Базовый URL
Все запросы к API отправляются на базовый URL:
```
http://localhost:8000/
```

## Эндпоинты

### 1. Посты
- **Список всех постов**
  - **URL**: `/posts/`
  - **Method**: `GET`
  - **Auth required**: Нет
  - **Описание**: Возвращает список всех постов.

- **Создание нового поста**
  - **URL**: `/posts/`
  - **Method**: `POST`
  - **Auth required**: Да
  - **Описание**: Создает новый пост. Требует аутентификации.
  - **Данные**: 
    ```json
    {
      "title": "Заголовок поста",
      "content": "Содержимое поста"
    }
    ```

- **Получение конкретного поста**
  - **URL**: `/posts/<id>/`
  - **Method**: `GET`
  - **Auth required**: Нет
  - **Описание**: Возвращает детали конкретного поста.

- **Обновление поста**
  - **URL**: `/posts/<id>/`
  - **Method**: `PUT` or `PATCH`
  - **Auth required**: Да
  - **Описание**: Обновляет информацию о посте. Требует аутентификации.
  - **Данные** (пример для `PATCH`):
    ```json
    {
      "title": "Новый заголовок"
    }
    ```

- **Удаление поста**
  - **URL**: `/posts/<id>/`
  - **Method**: `DELETE`
  - **Auth required**: Да
  - **Описание**: Удаляет пост. Требует аутентификации.

### 2. Комментарии
- **Добавление комментария к посту**
  - **URL**: `/posts/<post_id>/comments/`
  - **Method**: `POST`
  - **Auth required**: Да
  - **Описание**: Добавляет новый комментарий к указанному посту. Требует аутентификации.
  - **Данные**:
    ```json
    {
      "author_name": "Имя автора",
      "comment_text": "Текст комментария"
    }
    ```

## Форматы данных
- **Посты**: Объекты постов возвращаются в следующем формате:
  ```json
  {
    "id": 1,
    "title": "Заголовок поста",
    "content": "Содержимое поста",
    "published_date": "2023-01-01T12:00:00Z"
  }
  ```

- **Комментарии**: Объекты комментариев возвращаются в следующем формате:
  ```json
  {
    "id": 1,
    "post": 1,
    "author_name": "Имя автора",
    "comment_text": "Текст комментария",
    "created_date": "2023-01-02T12:00:00Z"
  }
  ```

## Аутентификация
- Для аутентификации используются токены. Для получения токена, отправьте POST запрос на `/api-token-auth/` с вашими учетными данными пользователя:
  ```json
  {
    "username": "логин_пользователя",
    "password": "пароль_пользователя"
  }
  ```
- Используйте полученный токен в заголовке запроса для аутентификации:
  ```
  Authorization: Token токен_пользователя
  ```
