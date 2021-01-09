FROM movecrew/one4ubot:alpine-latest

RUN mkdir /One4uBot && chmod 777 /One4uBot
ENV PATH="/One4uBot/bin:$PATH"
WORKDIR /One4uBot

RUN git clone https://github.com/4amparaboy/One4uBot -b sql-extended /One4uBot
RUN mkdir /4amparaboy && chmod 777 /4amparaboy
pip install faker --no-cache-dir
#
# Copies session and config(if it exists)
#
COPY ./sample_config.env ./userbot.session* ./config.env* /One4uBot/

#
# Make open port TCP
#
EXPOSE 80 443

#
# Finalization
#
CMD ["python3","-m","userbot"]
