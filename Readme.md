# MusicApp

My first Django project to create albums, add songs, and play music(Music player provided by lecturer(Java Script)).

## Features

- Create albums
- Add songs to albums
- Play music from the browser

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/Veselin33/MusicApp.git
cd MusicApp

2. ** Create and Activate venv**
    python -m venv .venv
    # Windows
    - .venv\Scripts\activate
    # macOS/Linux
    - source .venv/bin/activate

3. **Install Dependencies**
    pip install -r requirements.txt

4. **Apply Migrations**
    python manage.py migrate

5. **RUN**
    python manage.py runserver

6. **Access**
    Open http://127.0.0.1:8000/

