# Django Project

This is a simple Django project for managing products with a REST API and a frontend interface. 

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setup

Follow these steps to set up the project:

1. **Clone the repository**

    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Create and activate a virtual environment**

    ```
    python -m venv venv
    ```

    - On Windows:
      ```
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```
      source venv/bin/activate
      ```

3. **Install the required packages**

    ```
    pip install -r requirements.txt
    ```

4. **Apply database migrations**

    ```
    python manage.py migrate
    ```

## Running the Project

To start the development server:

```
python manage.py runserver
```
