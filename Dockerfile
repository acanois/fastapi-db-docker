FROM python:3.10

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./app /src/app

# CMD ["fastapi", "run", "app/main.py", "--host", "0.0.0.0", "--port", "80"]

# Via the docs: 
# If you are running your container behind a TLS Termination Proxy (load balancer) 
# like Nginx or Traefik, add the option --proxy-headers, this will tell Uvicorn 
# (through the FastAPI CLI) to trust the headers sent by that proxy telling it that 
# the application is running behind HTTPS, etc.
CMD ["fastapi", "run", "app/main.py", "--proxy-headers", "--port", "80"]
