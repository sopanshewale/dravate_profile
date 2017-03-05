FROM django 
RUN apt-get update
RUN apt-get install python-pip -y 
ADD ./dravate_profile  /app 
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python",  "manage.py", "runserver" ]

