# Team ranking board

```
    Author: Boitumelo Phetla
    DATE  : 11/04/2022 12:30
    Description: project outline and structure
```

## Assumptions

```
    1. input_file is named : league.txt
    2. input data is assumed to be of the right format, no need to implement handlers for input data
    3. input delimiters is assumed to be ', '
    4. input structure is assumed to be of format <str> name <int> score, <str> name <int> score
    5. entries are delimitered by a newline


    data input:
    Lions 4, Snakes 1
    Elephants 4, Lions 1
```


## How to run application

### via docker container
```
    $ docker build -t league:0.1 .
    $ docker run -i league:0.1
```

### via command line interface
navigate to app/
```
    $ python3 app/main.py
```

### how to run unittest
```
    $ python app/test_main.py
```


# project structure

```
    |---- Dockerfile
    |---- app/
    |     |_____main.py
    |     |_____league.txt
    |     |_____test_main.py
    |____README.md
```

