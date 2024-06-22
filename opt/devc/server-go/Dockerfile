ARG IMAGE_FROM=
FROM ${IMAGE_FROM}

COPY go.mod go.sum /tmp/mod/
RUN set -eux; \
    cd /tmp/mod \
    && go mod download

EXPOSE 8000

CMD [ "/bin/zsh" ]
