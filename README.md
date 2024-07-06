# ShareRide
ShareRide is a Django application which matches  users based on their travel schedule.

Users can submit requests sharing their travel plan.


![Share travel schedule](image_2.png)

Users can see their request status from home page.


![ShareRide](readme.png)


## Technologies
- Python 3.10
- Django
- Celery (with rabbitmq as broker)
- Docker
- HTML
- CSS

## Usage

1. Clone the repository:
   ```bash
    git clone https://github.com/FarzanRashid/ShareRide.git
    ```
2. Navigate to the project directory:
    ```bash
    cd /path/to/ShareRide
    ```

3. Create a .env file.


4. Configure the .env file by


4. Run the application
    ```bash
    docker compose up --build
    ```

5. Visit localhost:8000/signup/ for registration.
