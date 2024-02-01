# This is a simple command line exam flashcard app build with python

## Run 
    - python app.py

## Questions 
    - You can add your questions and answers to the 'questions.json' file

## Docker Build
    - Clone the repo and upstart the Docker Container with

    ```bash
    docker build -t flashcard_app .
    docker run --rm -ti flashcard_app
    ```

 ## TO-DO
    - Choose a limited random set of questions. 