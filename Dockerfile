FROM continuumio/miniconda3

WORKDIR /app
ENV FLASK_ENV development

COPY requirements.txt ./
RUN conda create -n ${FLASK_ENV} && conda install -n ${FLASK_ENV} --file requirements.txt
ENV PATH /opt/conda/envs/${FLASK_ENV}/bin:$PATH

COPY app.py .

EXPOSE 5000
ENTRYPOINT ["flask", "run"]