FROM python:3.6.7-stretch
RUN pip install flask numpy scipy scikit-learn && \
    mkdir /app
COPY app.py /app
COPY sentiment.pkl /app
WORKDIR /app
EXPOSE 8008
ENTRYPOINT ["python"]
CMD ["app.py"]