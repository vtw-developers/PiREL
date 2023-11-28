FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3 net-tools iputils-ping htop curl
RUN apt-get update && apt-get install -y python3-pip npm

# SHELL ["/bin/bash", "-l", "-euxo", "pipefail", "-c"]

ENV NVM_DIR /usr/local/nvm
ENV NODE_VERSION 16.15.1

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN mkdir -p /usr/local/nvm
ENV NODE_PATH $NVM_DIR/v$NODE_VERSION/lib/node_modules
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH


# Install nvm with node and npm
RUN curl -sL https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash \
  && . $NVM_DIR/nvm.sh \ 
  && nvm install $NODE_VERSION && nvm alias default $NODE_VERSION && nvm use default \
  && npm install -g nodemon

# RUN ln -sf $NVM_DIR/versions/node/v$NODE_VERSION/bin/node /usr/bin/nodejs
# RUN ln -sf $NVM_DIR/versions/node/v$NODE_VERSION/bin/node /usr/bin/node
# RUN ln -sf $NVM_DIR/versions/node/v$NODE_VERSION/bin/npm /usr/bin/npm

RUN node -v
RUN npm -v

COPY requirements.txt /root/requirements.txt
WORKDIR /root
RUN pip3 install -r requirements.txt
CMD python3