FROM sheercat/fbprophet

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install --upgrade pandas
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

EXPOSE 5000

CMD flask run --host=0.0.0.0