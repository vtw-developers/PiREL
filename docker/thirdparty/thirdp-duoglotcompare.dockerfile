FROM continuumio/anaconda3

RUN conda create -n py39 python=3.9
RUN conda create -n py38 python=3.8
RUN conda create -n py27 python=2.7

RUN conda run -n py39 pip install transcrypt==3.9.0
RUN conda run -n py38 pip install javascripthon==0.11 openai

WORKDIR /root/
COPY py2js.tar.gz /root/
RUN tar -xzvf py2js.tar.gz


# Install Node

RUN apt-get update && apt-get install -y net-tools iputils-ping htop curl

ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 16.15.1
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN mkdir -p /usr/local/nvm
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH

RUN curl -sL https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash \
  && . $NVM_DIR/nvm.sh \ 
  && nvm install $NODE_VERSION && nvm alias default $NODE_VERSION && nvm use default

RUN node -v
RUN npm -v

# Install OpenAI and unbuffer
RUN conda run -n base pip install openai==0.25
RUN apt-get update && apt-get install -y expect