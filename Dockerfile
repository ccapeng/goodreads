FROM python:3.7
EXPOSE 8000

RUN mkdir /build
WORKDIR /build

ENV SECRET_KEY fu8fQ5oGQEDlwiICw45dGSuxiu13STyIrxY0Rb6ibI 
ENV GOODREADS_KEY RDfV4oPehM6jNhxfNQzzQ

COPY . /build
RUN pip install -r requirements.txt

#CMD /bin/bash
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]