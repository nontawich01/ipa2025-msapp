FROM python
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install pymongo
COPY . .
CMD python3 scheduler.py  
