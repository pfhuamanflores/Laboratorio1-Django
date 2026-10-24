# Laboratory 1 - Web Application Development with Django

## Project Description

This project was developed as part of the **Enterprise Application Development** course to learn the fundamentals of Django and understand how to build web applications using Python.

The laboratory consists of two applications: a task management application and a basic calculator that performs mathematical operations using parameters provided through URLs.

## Technologies Used

- Python 3.14.6
- Django 6.1.2
- HTML
- SQLite
- Visual Studio Code
- Git and GitHub

## Features

### 1. Task Management Application (`tasks`)

This application uses a model called `Task`, which contains the following fields:

- `title`: Stores the task name.
- `completed`: Indicates whether the task has been completed.

The application also includes a view and an HTML template to display tasks in the web browser.

**Access URL:**

`http://localhost:8080/`

### 2. Mathematical Operations Application (`operaciones`)

This application performs three basic mathematical operations using two integers provided through the URL.

| Operation | Example URL | Result |
|---|---|---|
| Addition | `/app/sumar/18/19` | 37 |
| Subtraction | `/app/restar/18/19` | -1 |
| Multiplication | `/app/multiplicar/18/19` | 342 |

## Project Structure

```text
todoproject/
│
├── manage.py
├── .gitignore
│
├── todoproject/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── tasks/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── migrations/
│   └── templates/
│       └── tasks/
│           └── task_list.html
│
└── operaciones/
    ├── models.py
    ├── views.py
    └── urls.py
```

## Installation and Setup

Follow these steps to run the project locally.

**1. Clone the repository**

```bash
git clone https://github.com/pfhuamanflores/Laboratorio1-Django.git
```

**2. Navigate to the project directory**

```bash
cd Laboratorio1-Django
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment (Windows)**

```powershell
venv\Scripts\activate
```

**5. Install Django**

```bash
pip install Django==6.1.2
```

**6. Apply database migrations**

```bash
python manage.py migrate
```

**7. Start the development server**

```bash
python manage.py runserver 8080
```

**8. Open the application in your browser**

Visit:

`http://localhost:8080/`

## Expected Results

The mathematical operations application should display the following results:

**Addition**

```text
URL: http://localhost:8080/app/sumar/18/19
Output: La suma de 18 + 19 = 37
```

**Subtraction**

```text
URL: http://localhost:8080/app/restar/18/19
Output: La resta de 18 - 19 = -1
```

**Multiplication**

```text
URL: http://localhost:8080/app/multiplicar/18/19
Output: La multiplicación de 18 * 19 = 342
```

## Learning Outcomes

Through this laboratory, I learned how to configure a Django project, create applications, define models, manage database migrations, and implement views and URL routing.

I also gained practical experience using Visual Studio Code, Git, and GitHub to develop and manage a web application.

## Conclusions

1. I learned how to create and configure a web application using Django and Python.
2. I understood how models, views, and HTML templates work together in a Django application.
3. I learned how to use database migrations to create and manage database tables.
4. I successfully implemented mathematical operations using parameters received through URLs.
5. This laboratory helped me improve my web development skills and gain practical experience with Git and GitHub.

## Author

**Paulo Huaman**

GitHub: [pfhuamanflores](https://github.com/pfhuamanflores)

---

*This project was developed for educational purposes as part of the Enterprise Application Development course.*
