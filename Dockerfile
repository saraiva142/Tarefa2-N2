FROM python:3.8-slim

WORKDIR /app
COPY . .
#COPY app /app
RUN pip install pyodbc
#RUN pip install Bootstrap
RUN pip install Flask
#RUN pip install render_template
RUN pip install requests
RUN pip install Docker

#VOLUME /var/run/docker.sock

CMD [ "python", "script_cliente_http.py" ]
