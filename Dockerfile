FROM python:3.6-slim

COPY semesterstats ./semesterstats
COPY FormattedData ./FormattedData
COPY Resources ./Resources
COPY requirements.txt ./

RUN mkdir -p ./imported
RUN pip install -r requirements.txt && rm -rf /var/lib/apt/lists/*

CMD ["python", "-m", "semesterstats"]