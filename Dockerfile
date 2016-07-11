FROM akretion/voodoo:latest
USER root
RUN apt-get install libffi-dev
USER odoo
