FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app
COPY ./ml_model /code/ml_model

CMD ["fastapi", "run", "app/app.py", "--port", "80"]
#CMD ["uvicorn", "main:app", "--host=0.0.0.0" , "--reload" , "--port", "8000"]

##Build locally -> docker build -t say2imran/ml-model-language-detector:v1.0.0 .
##Run locally -> docker run -p 8888:80 say2imran/ml-model-language-detector:v1.0.0
