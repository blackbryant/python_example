FROM python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY . .
ADD ./requirements.txt .
EXPOSE 8000
RUN pip install -r requirements.txt
CMD ["python3", "manage.py","runserver","0.0.0.0:8000"]
