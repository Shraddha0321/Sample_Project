# Apollo.io Scraper API

## Introduction

This project is a FastAPI-based API that scrapes search results from Apollo.io. It provides two endpoints for initiating a scraping job and checking the status of the job.

## Tech Stack and Installation Instructions

### Tech Stack
- FastAPI
- Celery
- Redis (as Celery broker)
- Docker

### Installation Instructions
1. Clone this repository.
2. Install Docker and Docker Compose.
3. Run `docker-compose up --build` to build and start the application.
4. Access the API at `http://localhost:8000`.

## Conventions Used and Development Details

- The `/scrape` endpoint accepts POST requests with `name` and `organization_name` parameters to initiate a scraping job and returns a job ID.
- The `/scrape_results/{job_id}` endpoint accepts GET requests with a job ID to check the status of the job. If the job is finished, it returns the scraped results.
- Celery is used for asynchronous task processing to handle the scraping jobs in the background.
- Unit tests are written using Pytest and can be found in the `test_main.py` file.
