# IP Tracking: Security and Analytics

This project implements secure and privacy-aware IP tracking features using Django.  
It is part of the **ALX Backend Security** curriculum.

---

## Features
- Logs IP addresses, timestamps, and paths for all incoming requests.
- Blocks blacklisted IPs automatically.
- Uses geolocation data (country, city) for analytics.
- Applies rate-limiting to sensitive views.
- Detects anomalies and suspicious activity using Celery tasks.
- Maintains compliance with privacy and retention best practices.

---
## Project Structure

alx-backend-security/
├── manage.py
├── requirements.txt
├── README.md
├── alx_security_project/
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
└── ip_tracking/
├── middleware.py
├── models.py
├── views.py
├── tasks.py
└── management/
└── commands/
└── block_ip.py


---

## Setup Instructions
1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/alx-backend-security.git
   cd alx-backend-security

    Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Run migrations

python manage.py migrate

Start the development server

python manage.py runserver

Add a test IP to the blacklist (example)

    python manage.py block_ip 192.168.1.10

Environment Variables

Create a .env file in the project root (never commit it):

SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
GEOLOCATION_API_KEY=your-api-key

Then load it in settings.py using os.getenv.

