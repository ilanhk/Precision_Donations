# Precision Donations

Precision Donations is my first solo personal project and hackathon project. I built it around a question I kept coming back to: **how can someone choose where to donate based on need, rather than on which cause is most popular on social media?**

The idea is to bring information about world problems, the people affected by them, and the organizations working on them into one place. For diseases, the goal is to make serious, underfunded causes easier to notice: a disease with a high death toll and relatively little research funding should be more visible than one receiving attention simply because it is already well known.

## What it can do

- Browse diseases and view reported deaths, people affected, and research-lab funding.
- Filter disease statistics by year and country.
- View disease details and find research labs associated with a disease.
- Search for diseases, labs, and donors.
- Create donor or research-lab accounts and profiles.
- Let donors save labs to a favorites list.
- Explore early concept pages for other world problems, including climate change and world hunger.

## How the disease list is ordered

The current disease list orders diseases by the highest reported death count first, then by the lowest recorded funding when death counts are equal. The longer-term project goal is to help donors identify causes that are both serious and underfunded.

This is an early prototype, not a verified charity evaluator. Its usefulness depends on the accuracy, completeness, and comparability of the data entered into it. Rankings should not be treated as a definitive measure of impact or as a substitute for checking an organization’s work and financial reporting.

## Built with

- Python
- Django 3.1
- SQLite
- Bootstrap-based Django templates

The pinned dependencies are in [`requirements.txt`](requirements.txt). The project uses an older Django release, so Python 3.8 or 3.9 is recommended for the most compatible setup.

## Run locally

From the project directory, create and activate a virtual environment, install the dependencies, apply the database migrations, and start Django's development server.

### Windows PowerShell

```powershell
py -3.8 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser. To create an admin account for local development, run:

```powershell
python manage.py createsuperuser
```

The app uses SQLite and stores local database data in `db.sqlite3`. You will need relevant disease, country, statistics, and lab records for the comparison pages to show useful results.

## Sample data

The project includes a sample-data seeder in [`addtodatabase.py`](addtodatabase.py). It is intended to populate the database with countries, diseases, statistics, research labs, users, and categories. Run it after applying migrations:

```powershell
python addtodatabase.py
```

The seeder is an old prototype script. It fetches disease information from an external API and stops with a clear error if the request fails, the response is invalid, or fewer than 47 diseases are returned.

## Project status

This project was made as a solo learning and hackathon project. It is an initial implementation of the idea, not a production-ready donation platform. The next important steps would be improving the data sources and transparency, refining how need and funding are compared, and testing the experience with donors and research organizations.
