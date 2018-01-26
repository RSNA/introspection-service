# Token Introspector

An implementation of OAuth 2.0 Token Introspection specific to SMART on FHIR.

It take a token and attempts to use it to issue a FHIR `GET Patient` API call,
usin the result to determine whether the token is `active`. Eventually it may
offer other resoltion mechanisms (e.g. inspecting a vendor-specific JWT).


## Docker usage
Build and start a Docker containers using: 
```
docker build . -t <some-tag-name>
docker run  -p 9004:5000 <some-tag-name>:latest
```
This exposes the service on port 9004 of the local machine.

Test your connection using the CuRL command:
```
curl -d "token=<token value>&patient=<fhir pid>" -X POST http://localhost:9004/api/introspect
```
where the \<token\> and \<patient-id\> values must be known to the API server referenced in the Dockerfile.

## Installation

```
pip install .
```

## Configuration

Token Introspector checks the environment for:

+ **API_SERVER**: The FHIR server where tokens should be tried.

## Running

```
flask run
```
