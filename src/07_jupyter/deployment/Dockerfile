# Bystronic Jupyter Deployment
FROM jupyter/scipy-notebook:latest

LABEL maintainer="Daniel Senften <daniel.senften@bystronic.com>"
LABEL description="Bystronic Jupyter Environment für Produktionsanalyse"

USER root

# System-Abhängigkeiten installieren
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    git \
    vim \
    && rm -rf /var/lib/apt/lists/*

USER $NB_UID

# Python-Requirements kopieren und installieren
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Jupyter-Konfiguration kopieren
COPY jupyter_notebook_config.py /home/jovyan/.jupyter/

# JupyterLab Extensions installieren
RUN jupyter labextension install @jupyter-widgets/jupyterlab-manager \
    && jupyter labextension install @jupyterlab/toc \
    && jupyter labextension install @jupyterlab/git

# Notebooks und Beispiele kopieren
COPY notebooks/ /home/jovyan/work/
COPY examples/ /home/jovyan/examples/

# Arbeitsverzeichnis setzen
WORKDIR /home/jovyan/work

# Port freigeben
EXPOSE 8888

# Jupyter starten
CMD ["start-notebook.sh", \
     "--NotebookApp.token=''", \
     "--NotebookApp.password=''", \
     "--NotebookApp.allow_root=True"]
