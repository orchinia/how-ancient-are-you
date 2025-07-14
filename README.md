# How Ancient Are You

A fantasy-themed personality quiz that reveals your mental age and mythical race — from hobbits to elves to dwarves.

## Features

- Interactive web-based quiz built with Flask and Bootstrap
- Dynamic questions and results loaded from a MySQL database
- Dockerized for easy deployment
- Result mapping to fantasy races and ages

## Demo

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/)
- (Optional) Python 3.13+ and MySQL 8.0+ if running locally

### Quick Start (Recommended)

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/how-ancient-are-you.git
    cd how-ancient-are-you
    ```

2. Start the app with Docker Compose:
    ```sh
    docker-compose up --build
    ```

3. Visit [http://localhost:8888](http://localhost:8888) in your browser.

### Manual Setup

1. Install Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Set up a MySQL database (see `docker-compose.yml` for credentials).

3. Run the Flask app:
    ```sh
    python src/app.py
    ```

## Project Structure

```
src/
  app.py           # Flask application entry point
  models.py        # SQLAlchemy models and quiz logic
  templates/       # Jinja2 HTML templates
  static/          # Static files (CSS, JS, images)
requirements.txt   # Python dependencies
dockerfile         # Docker build instructions
docker-compose.yml # Multi-container setup (Flask + MySQL)
```

## Authors

- Hsin Chi Chu
- Jih Hung Huang

---

*This is a demo project for forms and web development with Flask and Docker.*

