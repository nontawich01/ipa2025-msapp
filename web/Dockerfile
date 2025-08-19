FROM python
RUN pip install flask 
RUN pip install pymongo
COPY ./sample_app.py .
COPY ./static ./static
COPY ./templates ./templates
EXPOSE 8080
CMD python3 sample_app.py  
