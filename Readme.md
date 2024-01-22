**FastApi with Celery and Redis**

- **FastApi** is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- **Celery** is a simple, flexible, and reliable distributed system to process vast amounts of messages, while providing operations with the tools required to maintain such a system.
- **Redis** is an open source (BSD licensed), in-memory data structure store, used as a database, cache, and message broker.

**Important Commands used in this project**:
- Docker compose command used: `docker-compose --file docker-compose.yml up --build -d` (detach mode build and run containers in background)
- Docker compose command used: `docker-compose --file docker-compose.yml down` (to stop the containers)
- Docker compose command used: `docker-compose --file docker-compose.yml up --build` (to build run the containers in foreground)
- Docker compose command used: `docker-compose --file docker-compose.yml logs -f` (to see the logs of the containers)
- Docker compose command used: `docker-compose --file docker-compose.yml exec <container_name> bash` (to enter into the container)
- Docker compose command used: `docker-compose --file docker-compose.yml up` (to run the containers in foreground)