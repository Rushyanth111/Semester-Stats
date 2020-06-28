FROM python:3.6-slim
RUN mkdir -p /project/imported
WORKDIR /project

# COPY STATIC FILES
COPY FormattedData ./FormattedData
COPY Resources ./Resources
COPY requirements.txt ./

#ENSURE THAT ALL DEPS ARE INSTALLED
RUN pip install -r requirements.txt && rm -rf /var/lib/apt/lists/*

#COPY PROJECT
COPY semesterstats ./semesterstats

CMD ["python", "-m", "semesterstats"]