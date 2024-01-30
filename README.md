## About

I'm planning on using this as the backend for my [blog project](https://github.com/tkbui/blog), which serves as a Next.js (React) frontend. For now I will probably mock data with .json files stored here until I set up cloud databases (MongoDB Data API + Vercel integration keeps failing on me... might need to look elsewhere) or when I am more comfortable using official 3rd party APIs to display data.

## Getting Started

This set up follows the following guide: https://www.youtube.com/watch?v=OwxxCibSFKk

- currently using Python 3.11.7 with pip
- currently developing on Windows 10

---

In a terminal while in the root folder (blog-backend):

#### 1. `python -m venv venv`

This creates the virtual environment in /venv ; this is needed on fresh clones since /venv is excluded due to .gitignore

#### 2. `.\venv\Scripts\activate.bat`

Activates the VE. To deactivate: `.\venv\Scripts\deactivate.bat`

#### 3. `touch server.py`

Create the server file (if not already existing) in the root folder. This will contain all of our Flask code.

#### 4. `touch requirements.txt`

Create a requirements.txt in root to hold our requirements -- creating this so that in the future, we can add and remove dependencies as needed and install in a single command. Add each dependency on its own line. For now, add 'flask' and 'flask-cors'.

> 'flask-cors' is needed to make requests from next.js server to python api - or else will get cross-origin issues; this allows other servers to make requests to python endpoints.

#### 5. `pip install -r requirements.txt`

Installs all dependencies in requirements.txt, each separated by a new line. Can also do pip install [...] for single installs.

## Running the backend server locally (in terminal)

1. `.\venv\Scripts\activate.bat` (if not done already)
2. `python server.py` runs the server (port 5000 by default, currently changed to 8080 based on tutorial suggesting 5000 has issues with CORS?)
