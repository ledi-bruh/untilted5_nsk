# Цифровой прорыв
@python3.9.13
@node18.18.0

    pip install -r ./requirements.txt

## backend

    cd ./backend

    python -m spacy download en_core_web_sm

    git clone https://github.com/patil-suraj/question_generation.git
    
    (или просто по ссылке скачать архив в ./backend)
    wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz

    (и распаковать там же)
    tar -xvf  s2v_reddit_2015_md.tar.gz

    python -m src

## rasa

    cd ./rasa
    rasa {run|shell}

## frontend

    cd ./client
    npm run start
