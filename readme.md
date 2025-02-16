# Event Management System

The application follows the MVC architecture to maintain separation of concerns.

**Language:**

- Python 3.12.5

**Dependencies:**

- tabulate==0.9.0

## Installation Instructions

1. **Clone the repository:**

    ```bash
    git clone https://github.com/CarlosM01/sistema-produccion-eventos.git
    cd sistema-gestion-eventos
    ```
2. **Install the project dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3. **Start the application:**
    ```bash
    python3 main.py
    ```

---

**Notes:**
* The application is currently vulnerable to SQL Injection.
* Consider hashing passwords.
* Consider adding an option to cancel form submissions.
* AttendeeController is not optimized.
* Some design patterns are inconsistent.
* Data transfer between components is not standardized (consider using only dictionaries).