INSTALL
=======
create a virtualenv
pip install -r requirements.txt
fab dev
python manage.py syncdb -all
python manage.py migrate --fake
python manage.py runserver

Add ING csv's with the following mapping:
column1=datum,column2=naam_omschrijving,column3=rekening,column4=tegenrekening,column5=code,column6=af_bij,column7=bedrag,column8=mutatiesoort,column9=mededelingen


USE
===
Import csv using the Django Admin interface
Import into RawData
Select the rows in RawData table, use action 'Process Data', now Rekeningen and Boekingen will be filled.