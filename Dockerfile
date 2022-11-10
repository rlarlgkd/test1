FROM python:3.7

# Install requirements
RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /home
# Set environment variables
ENV FLASK_APP=manage.py

# Add source code
ADD app /home/app
ADD requirements.txt /home
ADD manage.py /home

RUN python manage.py db init
RUN python manage.py db migrate
RUN python manage.py db upgrade

ADD migrations /home/migrations




# ENTRYPOINT
# ENTRYPOINT python manage.py run

EXPOSE 5000
#not sure if app:app works$ -> (MODULE_NAME):$(VARIABLE_NAME)
CMD ["gunicorn", "-b", "0.0.0.0:5000" ,"manage:app"]
