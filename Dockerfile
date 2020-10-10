FROM python:3.7-alpine as base

RUN mkdir /install
WORKDIR /install

COPY requirements.txt ./

RUN apk add --update --no-cache --virtual .build-deps \
    libxml2-dev libxslt-dev g++ gcc

RUN pip install --no-cache --prefix="/install" -r requirements.txt

FROM python:3.7-alpine

RUN apk add libxml2-dev libxslt-dev
COPY --from=base /install /usr/local
RUN mkdir -p /app/imported
WORKDIR /app
COPY . .

CMD ["uvicorn", "semesterstat:app", "--host", "0.0.0.0","--port", "9000"]