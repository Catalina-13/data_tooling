FROM python:3.11

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "world_happiness.py"]
