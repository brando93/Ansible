FROM jenkins/jenkins:lts

USER root

# Necesario para docker exec
RUN apt-get update && \
    apt-get install -y docker.io ssh && \
    rm -rf /var/lib/apt/lists/*

USER jenkins