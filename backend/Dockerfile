FROM python:3.12.3

WORKDIR /workdir

RUN apt-get install make
COPY Makefile .
COPY pyproject.toml .
RUN make deps

COPY . .
CMD make migrate
CMD make run
