FROM python:3.9.16-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "calc:app","--host","0.0.0.0","--port","8000"]