# PythonDavaX
DavaX python homework

Overview
The Math-Service API is a lightweight FastAPI application that exposes common mathematical operations (power, Fibonacci sequence, factorial) through a RESTful interface. The project includes:
    - A clean API layer built with FastAPI
    - A service façade for execution and persistence
    - A SQLite-based repository for storing request logs
    - A reusable calculator library with optimized implementations
    - A static web UI for demonstration purposes
    - Dockerfile for containerization
    - Kubernetes manifests for deployment

Architecture
+-----------------+      +------------------+      +---------------+
|   Client (UI)   | <--> | FastAPI Endpoints| <--> | MathService   |
|  (index.html)   |      +------------------+      +---------------+
+-----------------+               |                     |
                                   v                     v
                             +--------------+      +-----------+
                             | Repository   |      | Calculator|
                             | (SQLite DB)  |      | Library   |
                             +--------------+      +-----------+ 

Project Structure
Project/
├── api/
│   └── math_router.py           # FastAPI router definitions
├── services/
│   ├── math_service.py          # Service façade with persistence
│   └── calculator.py            # Pure math implementations
├── repository/
│   └── db_repository.py         # SQLAlchemy models & DB init
├── static/                      # Demo UI files
│   ├── index.html
│   ├── index.js
│   └── styles.css
├── k8s/                         # Kubernetes manifests
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
├── Dockerfile                   # Multi-stage build containerization
├── main.py                      # Application entrypoint & routing
├── requirements.txt             # Python dependencies
├── .flake8                      # Linting config
├── .autopep8                    # Formatting config
└── README.md                    # Project documentation (this file)

Components

API Layer
    Defines three endpoints under the /math prefix:
        POST /math/pow      → Compute arbitrary power operations
        GET  /math/fib/{n}  → Retrieve the nᵗʰ Fibonacci number
        GET  /math/fact/{n} → Compute factorial of n

    Validates inputs via Pydantic models and path parameters
    Executes computations in separate threads using anyio to avoid blocking the event loop

Service Layer
    Provides a single entrypoint MathService.execute(op, **params)
    Maps operation names (pow, fib, factorial) to Calculator methods
    Persists each request and result to the database via _save_to_db
    Facilitates future swapping of algorithms without touching API code

Repository & Persistence
    Defines a SQLAlchemy ORM model MathRequest for logging:
        id, operation, parameters, result, timestamp
    Uses SQLite (math.db) for simplicity
    init_db() creates tables at application startup if needed

Calculator Library
Implements:
    pow(base, exp) with validation for negative bases and fractional exponents
    fib(n) with an LRU cache (maxsize 2048) to accelerate repeated calls
    factorial(n) delegating to Python's built-in but with an upper bound guard

Static UI
    A simple HTML/CSS/JS interface to demonstrate the API
    Uses fetch to call the FastAPI endpoints and displays results

Configuration & Dependencies
    Python Version: 3.11 (specified in Dockerfile)
    Dependencies (in requirements.txt):
    FastAPI, Uvicorn, SQLAlchemy, Pydantic, AnyIO
    Linting & Formatting:
        .flake8 and autopep8 configs enforce a max line length of 88

Database Initialization
    On application startup, main.py checks for the existence of the math_requests table:
        insp = inspect(engine)
        if not insp.has_table("math_requests"):
            init_db()
    This ensures the in-process SQLite database is prepared before handling requests.

Running Locally
    Start the API:
         python -m uvicorn main:app --reload

Docker
    Multi-stage build to install dependencies separately
    Copies the site-packages from the builder into the final image
    Exposes port 8010

Kubernetes Deployment
    The k8s/ directory contains manifests to deploy the service to any Kubernetes cluster.

Deployment Manifest
    Creates a Deployment named pythondavax-deploy with 2 replicas
    Uses the container image gcr.io/secure-electron-465406-m2/pythondavax:latest
    Configures readiness and liveness probes on / port 8010

Service Manifest
    Defines a LoadBalancer Service named pythondavax-svc
    Forwards external port 80 to container port 8010

Ingress Manifest
    Exposes the service at pythondavax.com
    Uses GCE Ingress controller via annotation kubernetes.io/ingress.class: "gce"
    TLS and cert-manager annotations can be added as needed

Logging & Monitoring
    Application logs are printed to stdout (captured by Kubernetes/GKE logging stack)
    Add Prometheus or Cloud Monitoring instrumentation as needed