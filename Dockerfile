FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pipenv install --system -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . /code/