FROM pytorch/pytorch:1.1.0-cuda10.0-cudnn7.5-runtime

LABEL maintainer="Carson.Graham@OctoConsulting.com"

RUN pip install --upgrade pip

run pip install flask_cors transformers
RUN pip install boto3
RUN pip install nltk
RUN pip install pdfplumber
RUN pip install python-docx
RUN pip install pandas



RUN mkdir /inst
COPY . /inst/
EXPOSE 5000

 WORKDIR /inst/

# ENTRYPOINT ["python", "flask_app.py"]
ENTRYPOINT [ "python" ]
