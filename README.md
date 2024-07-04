# ShareRide
ShareRide is a Django-based application where users can  sign up, log in, and find other users 
who want to travel to the same location, from the same location, and at the same time. This helps facilitate ride-sharing and makes commuting more efficient and economical.
![ShareRide](readme.png)

## Features
- User registration and authentication
- Search for co-passengers based on location and time
- Secure data handling

## Prerequisites
- Python 3.8+
- Docker 

## Installation

1. Ensure you have Python 3.10 or above installed. If not, download and install Python from
   [python.org](https://www.python.org/downloads/).    


2. Ensure you have Docker installed. If not, install it from https://docs.docker.com/engine/install/


3. Clone the repository:
   ```bash
    git clone https://github.com/FarzanRashid/ShareRide.git
    ```
4. Navigate to the project directory:

    ```bash
    cd /path/to/ShareRide
    ```
5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Pull the latest rabbitmq docker image from docker hub
   ```bash
   docker pull rabbitmq
    ```

7. Pull postgres alpine docker images from docker hub
   ```bash
   docker pull postgres:alpine
    ```
8. Configure the .env file

## Usage

1. Navigate to the project directory:

    ```bash
    cd /path/to/ShareRide
    ```
2.  Run the application
    ```bash
    docker compose up --build
    ```
    
3. Open your browser


4. Go to localhost:8000/signup/ for registration


5.  Type localhost:8000/login/ in your browser url bar to login.


6. Navigate to localhost:8000/home/ to track your active and past requests.


7. Go to localhost:8000/request/ to find co-passengers based on your location and time.
