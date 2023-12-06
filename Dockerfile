FROM python:3.8-slim
COPY . /app
WORKDIR /app
RUN pip install pyodbc
#RUN pip install Bootstrap
RUN pip install Flask
#RUN pip install render_template
RUN pip install requests
RUN pip install Docker

CMD [ "python", "script_cliente_http.py" ]
