FROM python:3.8
COPY . ./
RUN pip3 install -r requirements.txt
EXPOSE 8501
ENTRYPOINT ["streamlit","run"]
CMD ["grocer_model.py"]