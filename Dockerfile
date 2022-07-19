FROM jrareas/python_app_base

WORKDIR /app


# RUN "pip3 install -r requirements.txt"

RUN pip3 install -e .

# CMD ["tail", "-f", "/dev/null"]

CMD ["pserve", "development.ini",  "--reload"]