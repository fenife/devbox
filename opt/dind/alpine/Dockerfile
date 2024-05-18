FROM alpine:3.19

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories 
RUN apk -U add bash netcat-openbsd \
    && rm -rf /var/cache/apk/*

CMD [ "/bin/bash" ]

