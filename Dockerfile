FROM python:3.6-slim
RUN mkdir -p /project/imported
WORKDIR /project

# COPY STATIC FILES
COPY requirements.txt ./

#ENSURE THAT ALL DEPS ARE INSTALLED
RUN pip install -r requirements.txt && rm -rf /var/lib/apt/lists/*

#COPY PROJECT
COPY semesterstats ./semesterstats
COPY Resources ./Resources
COPY FormattedData ./FormattedData

CMD ["python", "-m", "semesterstats"]