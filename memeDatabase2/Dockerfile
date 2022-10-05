FROM python:3.10-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirments.txt /requirments.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip insall -r /requirments.txt
RUN apk del .tmp

RUN mkdir /memeEngine
COPY ./memeEngine /memeEngine
WORKDIR /memeEngine
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chown -R 755 /vol/web
USER user 

CMD ["entrypoint.sh"]