# Placeholder Dockerfile for Analytics Service
FROM public.ecr.aws/lambda/python:3.11

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py ./
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
