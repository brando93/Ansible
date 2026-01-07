FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    docker.io \
    openssh-server \
    iproute2 \
    ca-certificates \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /var/run/sshd

# Crear carpeta SSH
RUN mkdir -p /root/.ssh

# Copiar authorized_keys
COPY authorized_keys /root/.ssh/authorized_keys

# Permisos correctos (CRÍTICO)
RUN chmod 700 /root/.ssh && \
    chmod 600 /root/.ssh/authorized_keys

# Permitir login root (solo lab)
RUN echo 'root:root' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config

EXPOSE 22

CMD dockerd & /usr/sbin/sshd -D
