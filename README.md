# NumbersAPI API

This Django API client was created to give number trivia serving coming from [NumbersAPI](http://www.numbersapi.com/) a new spin.

## Setup

### Using Docker

TODO

### Without Docker

TODO

## Usage

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
