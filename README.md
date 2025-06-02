# Analytics Data Ingestion & Profiling Platform

A Flask-based web application for uploading CSV files, storing them in a PostgreSQL database, profiling the data, running SQL queries, and exporting datasets in multiple formats. It also includes Airflow DAGs for scheduled ingestion and Docker support for deployment.

---

## 🌐 Features

* Upload CSV files and automatically create PostgreSQL tables
* View dataset statistics: row count, column types, null values, unique values
* Drop empty columns with one click
* Run SQL queries on uploaded data
* Download data in CSV, Parquet, or TXT format
* Pre-load a sample dataset at startup
* Scheduled ingestion via Apache Airflow (@hourly)
* Dockerized deployment with Docker Compose

---

## 🚀 Quick Start (Docker)

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <project-directory>
```

### 2. Place your CSV

Put your main CSV file (e.g., `fact_resultats_epreuves.csv`) into a `shared_data/` folder at the root level.

### 3. Build and start the project

```bash
docker-compose up --build
```

### 4. Access the web app

Navigate to [http://localhost:5000](http://localhost:5000)

### 5. Access Airflow UI (if enabled)

Navigate to [http://localhost:8080](http://localhost:8080)

---

## 📂 Project Structure

```
├── app.py                 # Flask app
├── load_data_once.py      # Initial one-time data loader
├── ingest_csv_dag.py      # Airflow DAG for scheduled CSV ingestion
├── requirements.txt       # Python dependencies
├── Dockerfile             # Flask app Docker image
├── docker-compose.yml     # Docker Compose for services
├── shared_data/           # Folder for uploaded CSV files
```

---

## 🔧 Manual Setup (Optional)

### 1. Create virtual environment and install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Start PostgreSQL locally or via Docker

Make sure a PostgreSQL DB is available with:

* user: `user`
* password: `password`
* host: `localhost` or `db` (in Docker)
* database: `sportsdb`

### 3. Run the Flask app

```bash
python app.py
```

---

## 📊 Data Profiling

When a CSV is uploaded:

* A table is created in PostgreSQL
* Data types are inferred
* Null and unique values are counted per column
* Metadata is saved to the session
* First 20 rows are previewed in the web interface

---

## ⌛ Scheduled Ingestion with Airflow

* DAG file: `ingest_csv_dag.py`
* Runs hourly to ingest `fact_resultats_epreuves.csv` into PostgreSQL
* Requires Airflow service to be configured in `docker-compose.yml`

---

## 🚧 Improvements To-Do (Optional)

* Add data validation before inserting into DB
* User authentication for data upload/query
* Improve frontend display (charts, filters)
* Metadata logging (timestamps, actions)
* Add test suite (e.g., `pytest`, CI integration)

---

## 📄 License

This project is open-source and free to use for educational and demonstration purposes.
