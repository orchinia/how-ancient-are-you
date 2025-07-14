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
- (Optional) Make.exe to use Makefile

### Quick Start (Recommended)

1. Clone the repository:
    ```sh
    git clone https://github.com/orchinia/how-ancient-are-you.git
    cd how-ancient-are-you
    ```

2. Start the database(sql) host:
    ```sh
    make start-mysql
    ```
3. Start the web(flask) host:
    ```sh
    make build-host
    make start-host
    ```

3. Import Demo data to DB:
    ```sh
    // 1. get into web host terminal
    make host-shell
    // 2. run src/script.py to import data/{table}.csv to mysql
    python src/scrip.py
    ```

4. Visit [http://localhost:8888](http://localhost:8888) in your browser.

### Manual Setup

1. Install Python dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Set up a MySQL database (see `Makefile` for more details).

3. Run the Flask app:
    ```sh
    python src/app.py
    ```

## Project Structure

```
src/
  app.py           # Flask application entry point
  models.py        # SQLAlchemy models and quiz logic
  host.yaml        # Customized config file for the host, specified MYSQL_HOST ip address & port
  templates/       # Jinja2 HTML templates
  static/          # Static files (CSS, JS, images)
requirements.txt   # Python dependencies
dockerfile         # Docker build instructions
Makefile           # Automation commands for building, running, and managing the app and database
```

## Authors

- Hsin Chi Chu
- Jih Hung Huang

---

*This is a demo project for forms and web development with Flask and Docker.*

