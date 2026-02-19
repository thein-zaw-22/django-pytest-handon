# Django + pytest Learning Environment

This project is a complete Django testing playground that demonstrates modern pytest-based testing with realistic app code.

It includes:
- A sample Django app (`blog`) with model, views, URL routing, admin registration, and migration
- A pytest setup using `pytest-django`
- Database tests, client tests, fixture usage, and factory usage
- Coverage-ready test commands

### 🚀 Quick Guide: Test Flow & Reporting

**1. Execution Flow (Layers):**
- **Smoke Tests (Smoke):** Does the app start? (`test_smoke.py`)
- **Model Tests (Unit):** Does the database save data? (`test_models.py`)
- **View Tests (Integration):** Do URLs load successfully? (`test_views.py`)
- **API Tests (Functional):** Is the content correct? (`test_api.py`)

**2. Reporting Options:**
- **Terminal:** Quick pass/fail feedback.
- **Coverage:** Shows how much code is tested (%).
- **HTML:** A visual dashboard of results.

---

## 1. Project Goals

This repository is designed to teach practical best practices for using Django with pytest:

1. Configure `pytest-django` correctly
2. Build a realistic app (`Post` model + class-based views)
3. Write clear, maintainable tests
4. Reuse setup via fixtures and factories
5. Run everything immediately with minimal setup

---

## 2. Tech Stack

- Python 3.12+
- Django 6.0.2
- pytest 9.0.2
- pytest-django 4.11.1
- pytest-cov 6.0.0
- factory-boy 3.3.3
- Faker 36.1.1
- SQLite (default local database)

Dependencies are pinned in `/Users/theinzaw/Code/django-handon/requirements.txt`.

---

## 3. Directory Structure

```text
/Users/theinzaw/Code/django-handon/
├── manage.py
├── requirements.txt
├── pytest.ini
├── README.md
├── payhappy/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── apps/
│   ├── __init__.py
│   └── blog/
│       ├── __init__.py
│       ├── apps.py
│       ├── models.py
│       ├── admin.py
│       ├── views.py
│       ├── urls.py
│       ├── factories.py
│       ├── migrations/
│       │   ├── __init__.py
│       │   └── 0001_initial.py
│       └── tests/
│           ├── __init__.py
│           ├── test_models.py
│           ├── test_views.py
│           └── test_api.py
└── tests/
    ├── conftest.py
    └── test_smoke.py
```

---

## 4. Quick Start

From project root (`/Users/theinzaw/Code/django-handon`):

```bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open:
- App routes: [http://127.0.0.1:8000/posts/](http://127.0.0.1:8000/posts/)
- Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

Create admin user:

```bash
python manage.py createsuperuser
```

---

## 5. Running Tests

### Run all tests

```bash
pytest
```

### Run with coverage

```bash
pytest --cov=apps --cov-report=term-missing
```

### Generate HTML coverage visualization

```bash
pytest --cov=apps --cov-report=html --cov-report=term-missing
```

Open the generated report:
- `/Users/theinzaw/Code/django-handon/htmlcov/index.html`

### Optional: Generate an HTML test result report (pass/fail dashboard)

Install plugin:

```bash
python -m pip install pytest-html
```

Generate report:

```bash
pytest --html=reports/pytest_report.html --self-contained-html
```

Open:
- `/Users/theinzaw/Code/django-handon/reports/pytest_report.html`

### Run only one file

```bash
pytest apps/blog/tests/test_views.py
```

### Run one test function

```bash
pytest apps/blog/tests/test_views.py::test_post_detail_view_returns_404_for_missing_post
```

---

## 6. Pytest Configuration

`/Users/theinzaw/Code/django-handon/pytest.ini`:

- `DJANGO_SETTINGS_MODULE = payhappy.settings`
  - Tells `pytest-django` which Django settings to load
- `testpaths = apps tests`
  - Limits discovery to app-level tests and project-level tests
- `python_files = test_*.py *_tests.py tests.py`
  - Standard naming patterns
- `addopts = -ra --strict-markers --disable-warnings`
  - Better output and stricter marker behavior

---

## 7. Application Walkthrough

### 7.1 Model: `Post`

Defined in `/Users/theinzaw/Code/django-handon/apps/blog/models.py`.

Fields:
- `title` (`CharField`)
- `content` (`TextField`)
- `is_published` (`BooleanField`)
- `created_at` (`DateTimeField(auto_now_add=True)`)

Best practices demonstrated:
- `__str__` for readable admin/debug output
- `Meta.ordering = ["-created_at"]` to keep newest posts first by default

### 7.2 Admin registration

`/Users/theinzaw/Code/django-handon/apps/blog/admin.py` registers `Post` with:
- list columns
- filters
- search fields

This is useful in real projects to inspect and manage content quickly.

### 7.3 Views

`/Users/theinzaw/Code/django-handon/apps/blog/views.py` provides:

- `PostListView` (`ListView`)
  - Returns only published posts
  - Uses plain `HttpResponse` for simple, template-free testing
- `PostDetailView` (`DetailView`)
  - Returns one published post by primary key
  - Returns 404 for missing/unpublished posts due to filtered queryset

### 7.4 URL routing

- Root include in `/Users/theinzaw/Code/django-handon/payhappy/urls.py`
- App routes in `/Users/theinzaw/Code/django-handon/apps/blog/urls.py`

Endpoints:
- `/posts/`
- `/posts/<int:pk>/`

---

## 8. Factories and Fixtures

### 8.1 Factory: `PostFactory`

Defined in `/Users/theinzaw/Code/django-handon/apps/blog/factories.py`.

Why this matters:
- Keeps test setup concise
- Generates realistic data with Faker
- Makes tests easier to read and maintain

Example use:

```python
PostFactory.create_batch(3, is_published=True)
```

### 8.2 Shared fixtures in `tests/conftest.py`

Defined in `/Users/theinzaw/Code/django-handon/tests/conftest.py`:

- `user`: creates a test user via `django_user_model`
- `authenticated_client`: logged-in Django test client
- `post`: one factory-created `Post`

Why this is good practice:
- Reduces duplication across tests
- Centralizes common setup
- Keeps test functions focused on behavior

---

## 9. Test Suite Walkthrough

### 9.1 Model tests
File: `/Users/theinzaw/Code/django-handon/apps/blog/tests/test_models.py`

Covers:
- record creation
- `__str__` behavior

### 9.2 View tests
File: `/Users/theinzaw/Code/django-handon/apps/blog/tests/test_views.py`

Covers:
- list endpoint returns HTTP 200
- detail endpoint returns HTTP 200 for existing post
- detail endpoint returns HTTP 404 for missing post

### 9.3 Response-count test
File: `/Users/theinzaw/Code/django-handon/apps/blog/tests/test_api.py`

Covers:
- creating multiple posts
- verifying list response shows correct published count

### 9.4 Smoke test
File: `/Users/theinzaw/Code/django-handon/tests/test_smoke.py`

Covers:
- minimal project boot sanity check

---

## 10. Why `@pytest.mark.django_db` Is Used

Any test that reads/writes the database must be marked with `@pytest.mark.django_db` (or use database fixtures). Without it, pytest-django blocks DB access by design.

This makes DB usage explicit and keeps pure unit tests fast.

---

## 11. Learning Notes and Best Practices

1. Prefer pytest function tests over `unittest.TestCase` for simpler, more readable tests.
2. Use fixtures for reusable setup, not copy-paste setup in every test.
3. Use factories for model data creation to avoid brittle hand-crafted objects.
4. Keep assertions direct and behavior-focused.
5. Test happy paths and failure paths (`404`, filtering behavior, etc.).
6. Keep app boundaries clean (`models.py`, `views.py`, `urls.py`, `tests/`).

---

## 12. Troubleshooting

### `pytest` command not found
Use:

```bash
python -m pytest
```

### Database-related test error
Ensure migrations ran:

```bash
python manage.py migrate
```

### Admin login fails
No default admin password exists. Create one:

```bash
python manage.py createsuperuser
```

---

## 13. One-Command Dev/Test Flow (Reference)

```bash
python -m pip install -r requirements.txt
python manage.py migrate
pytest --cov=apps --cov-report=term-missing
python manage.py runserver
```

## 14. Visual Report Quick Commands

Coverage HTML report:

```bash
pytest --cov=apps --cov-report=html --cov-report=term-missing
```

Optional full HTML test report (`pytest-html`):

```bash
python -m pip install pytest-html
pytest --html=reports/pytest_report.html --self-contained-html
```
