FROM akretion/voodoo:latest
USER root
RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y libffi-dev && \
    apt-get clean
USER odoo
