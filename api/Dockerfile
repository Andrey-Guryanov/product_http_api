FROM python:3.10.8
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
RUN mkdir /api_service
WORKDIR /api_service
COPY [".env", "."]
COPY ["./api", "."]
RUN pip3 install -r /api_service/requirements.txt
CMD ["python", "run_api.py"]