FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies (minimal)
RUN apt-get update \
    && apt-get install -y --no-install-recommends curl build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker layer caching
COPY requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app ./app

# Default environment variables (can be overridden)
ENV PORT=8000

# Expose application port
EXPOSE 8000

# The actual command is set in docker-compose for dev to enable auto-reload
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


