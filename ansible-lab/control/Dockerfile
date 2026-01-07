FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

# Instalar herramientas base + Docker CLI + Python + pip
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    ssh \
    git \
    curl \
    sudo \
    docker.io \
    && rm -rf /var/lib/apt/lists/*

# Instalar Ansible y librería Python de Docker
RUN pip3 install --upgrade pip \
    && pip3 install ansible docker ansible-core

# Instalar colección community.docker
RUN ansible-galaxy collection install community.docker

# Copiar llaves SSH
RUN mkdir -p /root/.ssh
COPY id_ed25519 /root/.ssh/id_ed25519
COPY id_ed25519.pub /root/.ssh/id_ed25519.pub
RUN chmod 600 /root/.ssh/id_ed25519 && chmod 644 /root/.ssh/id_ed25519.pub

# Directorio de trabajo
WORKDIR /ansible

# Mantener vivo para Jenkins
CMD ["sleep", "infinity"]