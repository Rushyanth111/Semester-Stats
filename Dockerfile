FROM python:3.6-slim
RUN mkdir -p /project
WORKDIR /project
COPY semesterstats ./semesterstats
COPY FormattedData ./FormattedData
COPY Resources ./Resources
COPY requirements.txt ./

RUN pip install -r requirements.txt && rm -rf /var/lib/apt/lists/*

CMD ["python", "-m", "semesterstats"]