# Installation Python Base.
FROM python:3.7-alpine as install_image

# Install folder for installation of python packages and compilation.
RUN mkdir /install
WORKDIR /install

# Copy the requirements.
COPY requirements.txt ./

# Install dev dependencies and compilers.
RUN apk add --update --no-cache --virtual .build-deps \
    libxml2-dev libxslt-dev g++ gcc

# Run the installation.
RUN pip install --no-cache --prefix="/install" -r requirements.txt


# Running Image
FROM python:3.7-alpine


# Adding xml2-dev and xslt-dev for the python-deps.
# Adding TinyProxy for Proxy
RUN apk add libxml2-dev libxslt-dev nginx supervisor


# Semesterweb files Here.
RUN mkdir -p /web
COPY dist /web

# Semesterstat  Files Here:
WORKDIR /app
RUN mkdir -p /app/imported
RUN mkdir -p /app/semesterstat
COPY --from=install_image /install /usr/local
COPY semesterstat /app/semesterstat
COPY config.ini /app


# Nginx Configs Here.
RUN mkdir -p /run/nginx
RUN rm /etc/nginx/conf.d/default.conf
COPY Dockerfile.config/nginx.conf /etc/nginx/nginx.conf


# Supervisor Configs Here.
COPY Dockerfile.config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf


# Command to Run Supervisor.
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]