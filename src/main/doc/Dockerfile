#FROM ubuntu
FROM yaqwsx/kikit

RUN apt update \
    && apt install -y software-properties-common \
    && apt-get update \
    && apt-get install -y python3-pip python3-venv git
RUN python3 -m pip install sphinx sphinx-autobuild

RUN mkdir -p /home/doc \
    && groupadd doc \
    && useradd doc -g doc -d /home/doc \
    && chown doc:doc /home/doc 

RUN mkdir /workspace \
    && chown -R doc:doc /workspace
USER doc
WORKDIR /workspace
COPY --chown=doc:doc src/main/doc/requirements.txt ./documentation/src/main/doc/requirements.txt
RUN pip3 install -r documentation/src/main/doc/requirements.txt
# Install sphinx-pcbdraw
COPY --chown=doc:doc . ./documentation/
RUN git clone https://github.com/nobodywasishere/sphinx-pcbdraw.git ./documentation/src/main/dependencies/sphinx-pcbdraw
WORKDIR documentation
ENV PATH="$PATH:/home/doc/.local/bin"
#RUN sphinx-build src/main/doc doc