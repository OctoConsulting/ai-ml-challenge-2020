FROM pytorch/pytorch:latest

LABEL maintainer="Carson.Graham@OctoConsulting.com"

RUN pip install --no-cache-dir --upgrade pip

run pip install --no-cache-dir flask_cors transformers
RUN pip install --no-cache-dir boto3
RUN pip install --no-cache-dir nltk
#RUN pip install pdfplumber
RUN pip install --no-cache-dir pdfplumber==0.5.22
RUN pip install python-docx
RUN pip install pandas
RUN pip install googledrivedownloader

RUN mkdir -p /inst/testdata/uploads
COPY * /inst/
COPY ./nltk_data/ /nltk_data/
EXPOSE 5000

 WORKDIR /inst/

# ENTRYPOINT ["python", "flask_app.py"]
ENTRYPOINT [ "python" ]
