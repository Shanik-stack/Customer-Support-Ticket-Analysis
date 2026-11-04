
FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml .
COPY src/ ./src/

RUN pip install --no-cache-dir .

COPY data/ ./data/
COPY tests/ ./tests/

#Runs the main file
CMD ["python", "-m", "customer_support_tickets.main"] 
