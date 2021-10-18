# NumbersAPI API

This Django API client was created to give number trivia serving coming from [NumbersAPI](http://www.numbersapi.com/) a new spin.

## Setup

### Using Docker

Make sure that the Docker environment is properly installed and launched in your OS. Be certain to install a version that contains the `docker-compose` CLI as well.

To run and start your API server, run the following command in your project root folder. You can lose the `--build` flag after the first run:

```shell
docker-compose up --build
```

### Without Docker

Make sure that `python3 >= 3.8` is installed in your OS. It's recommended to setup a virtual environment for this project, so create a new directory and start it there by using `venv`.

```shell
python3 -m venv .
source bin/activate
```

Clone this repository inside the created directory, install the required `pip` packages and start your python server.

```shell
cd numbersapi_api
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0:8000
```

## Usage

You can access an website example inside the project at [http://localhost:8000](http://localhost:8000) and may take a look at its HTML file content on `api/templates/index.html`.

> ⚠️ **Warning**: This project is intended and configured for local development only. If you plan to use it in production, make sure that the Django `settings.py` file is properly patched for it.

There is only one route on this API, accessible via GET at [http://localhost:8000/api/get_fact](http://localhost:8000/api/get_fact), in which the following variety of parameters can be informed:

- **number**: the number whose fact will be retrieved, can be either an integer number or the word "random". Use the **day** and **month** parameters instead when requesting the "date" fact type. Default: "random"
- **fact_type**: the type of the fact, should be one of the following: "trivia", "math", "year" and "date". Default: "trivia"
- **month**: when the fact type is a "date", this needs to be informed, with a valid month from 1-12.
- **day**: when the fact type is a "date", this needs to be informed, with a valid day from 1-31.
- **fragment**: sets the fact text to return as a fragment to be used inside a sentence, no value needed.
- **default**: text to be retrieved when the queried number
  is not found. Default: `n` is a boring number.
- **notfound**: informs what should be done when the number
  is not found, should be one of the following: "default", "floor" (rounds the number to the next lowest found) and "ceil" (rounds the number to the next highest found). Default: the **default** parameter value
- **min**: sets a lower integer threshold to the "random" number, should be used along with the **max** parameter.
- **max**: sets a higher integer threshold to the "random" number, should be used along with the **min** parameter.

### Response

This route's response will be a JSON object containing the following fields:

- **text** (omitted when there is an error)
- **type** (omitted when there is an error)
- **number** (omitted when there is an error)
- **error** (empty when the request was successful)
