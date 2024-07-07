ARG IMAGE_FROM=
FROM ${IMAGE_FROM}

ENV PIP_CACHE_DIR=/wine/cache/pip

# 先安装必须依赖，否则后面会报错
RUN --mount=type=cache,target=${PIP_CACHE_DIR} \
    pip2 install --no-deps pbr==1.8 Paste==2.0.2 PasteDeploy==1.5.0 aioeventlet==0.5.2

COPY requirements.txt /tmp/
RUN --mount=type=cache,target=${PIP_CACHE_DIR} \
    pip2 install --no-deps -r /tmp/requirements.txt

# RUN pip2 install --no-deps argparse==1.4.0

ENV CODE_DIR=/wine/code/neutron
ENV PYTHONPATH="$PYTHONPATH:${CODE_DIR}"

WORKDIR /wine/devbox/opt/devc/neutron

CMD [ "/bin/zsh" ]
