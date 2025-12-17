# TodoWoo 📝

TodoWoo is a full-featured task management REST API built with Django and Django REST Framework. It provides secure user authentication and complete CRUD operations for managing personal todo items.

## ✨ Features

- **User Authentication**
  - User registration (signup)
  - User login with token-based authentication
  - Secure password handling

- **Todo Management**
  - Create new todos with title, memo, and importance flag
  - View all active (incomplete) todos
  - View all completed todos
  - Update existing todos
  - Delete todos
  - Mark todos as complete with automatic timestamp

- **User-Specific Data**
  - Each user can only access their own todos
  - Authentication required for all todo operations

## 🛠️ Tech Stack

- **Backend Framework**: Django
- **API Framework**:  Django REST Framework
- **Database**:  SQLite3 (default, easily switchable to PostgreSQL/MySQL)
- **Authentication**: Token-based authentication
- **Python**:  3.x

## 📋 API Endpoints

### Authentication
- `POST /api/signup` - Register a new user
- `POST /api/login` - Login and receive authentication token

### Todos
- `GET /api/todos` - List all active todos (incomplete)
- `POST /api/todos` - Create a new todo
- `GET /api/todos/<id>` - Retrieve a specific todo
- `PUT /api/todos/<id>` - Update a todo
- `DELETE /api/todos/<id>` - Delete a todo
- `POST /api/todos/<id>/complete` - Mark a todo as complete
- `GET /api/todos/completed` - List all completed todos

## 🗂️ Project Structure

```
TodoWoo/
├── API/                    # API application
│   ├── serializers.py     # DRF serializers for data validation
│   ├── views.py           # API views and endpoints
│   └── urls.py            # API URL routing
├── todo/                  # Todo model application
│   └── models.py          # Todo data model
├── todowoo/               # Main project settings
├── manage.py              # Django management script
└── db.sqlite3             # SQLite database
```

## 📊 Data Model

### Todo Model
- `title` (CharField) - Todo title (max 100 characters)
- `memo` (TextField) - Optional detailed description
- `created` (DateTimeField) - Auto-generated creation timestamp
- `datecompleted` (DateTimeField) - Completion timestamp (null until completed)
- `important` (BooleanField) - Priority flag (default: False)
- `user` (ForeignKey) - Associated user (cascading delete)

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MjdAkel/TodoWoo. git
   cd TodoWoo
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/`

## 📝 Usage Examples

### Register a new user
```bash
curl -X POST http://localhost:8000/api/signup \
  -H "Content-Type: application/json" \
  -d '{"username": "johndoe", "password": "securepass123"}'
```

### Login
```bash
curl -X POST http://localhost:8000/api/login \
  -H "Content-Type: application/json" \
  -d '{"username": "johndoe", "password": "securepass123"}'
```

### Create a todo
```bash
curl -X POST http://localhost:8000/api/todos \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type:  application/json" \
  -d '{"title": "Buy groceries", "memo": "Milk, eggs, bread", "important":  true}'
```

### List active todos
```bash
curl -X GET http://localhost:8000/api/todos \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

### Complete a todo
```bash
curl -X POST http://localhost:8000/api/todos/1/complete \
  -H "Authorization:  Token YOUR_TOKEN_HERE"
```

## 🔒 Security Features

- Password hashing using Django's built-in authentication
- Token-based authentication for API access
- CSRF protection for authentication endpoints
- User-specific data isolation (users can only access their own todos)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**MjdAkel**
- GitHub: [@MjdAkel](https://github.com/MjdAkel)

## 🙏 Acknowledgments

- Built with [Django](https://www.djangoproject.com/)
- REST API powered by [Django REST Framework](https://www.django-rest-framework.org/)

---

⭐ Star this repository if you find it helpful! 
