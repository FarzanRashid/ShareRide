# ShareRide
ShareRide is a Django-based application where users can find another user based on their travel
schedule. Users can submit a request to find a co-passenger who matches their travel plans.
![ShareRide](readme.png)


## Technologies
- Python 3.10
- Django
- Celery (with rabbitmq)
- Docker
- HTML
- CSS

## Usage

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

5. Configure the .env file


6. Run the application
    ```bash
    docker compose up --build
    ```
    
7. Go to localhost:8000/signup/ for registration.
