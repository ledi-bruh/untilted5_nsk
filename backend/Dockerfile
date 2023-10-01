FROM python:3.9-slim-buster

WORKDIR /backend

COPY . /backend

RUN apt-get update && apt-get install -y git

RUN pip install -r /backend/requirements.txt

RUN git clone https://github.com/AMontgomerie/question_generator.git

EXPOSE 80

ENV NAME env

CMD ["uvicorn", "__main__", "--host", "0.0.0.0", "--port", "80"]
