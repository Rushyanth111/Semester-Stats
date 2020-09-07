FROM python:3.7-slim
RUN mkdir -p /project/imported
WORKDIR /project

# COPY STATIC FILES
COPY requirements.txt ./

#ENSURE THAT ALL DEPS ARE INSTALLED
RUN pip install -r requirements.txt && rm -rf /var/lib/apt/lists/*

#COPY PROJECT
COPY semesterstat ./semesterstat

CMD ["python", "-m", "semesterstat"]