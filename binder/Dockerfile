#Sample Notebook https://mybinder.readthedocs.io/en/latest/tutorials/dockerfile.html
FROM jupyter/minimal-notebook:7f1482f5a136
RUN pip install git+https://github.com/grading/gradememaybe.git

# Make sure the contents of our repo are in ${HOME}
COPY . ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}
