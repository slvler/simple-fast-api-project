FROM python:3.8-slim-buster
WORKDIR /app
COPY . ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
