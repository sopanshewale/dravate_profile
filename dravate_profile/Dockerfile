FROM django 
RUN apt-get update
RUN apt-get install python3-pip vim -y 
ADD ./dravate_profile  /app 
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN chmod +x runserver.sh
CMD ["./runserver.sh" ]

