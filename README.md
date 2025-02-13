# crewAI
Exemple of migration from agentic towards CrewAI 

# Architecture
![img.png](doc/docker.png)


This application run a multi-container application implemented as two microservices:
- view-service
- summarizer-service
## The View service
User interface implemented with `streamlit`. It allows a user to 
upload a file and view the result.
Supported uploaded file as a .text format.

## The Summarizer service
Two agents are implemented with `crewai` framework.
The first one make an abstract from a CV
The second convert textual period of times into a formated period of times.

# Project files organization
![img.png](doc/projectfile.png)

# Configuration
Each service get its own configuration.
The `summarizer` service uses agents that invoke LLMs for accomplishing their tasks.
LLM keys has to be defined into `crewai/summarizer/.env` file:
```
MODEL=gpt-4o
OPENAI_API_KEY=<TO_BE_ASSIGNED>
```
For OpenAI, access API keys from :
> https://platform.openai.com/settings/organization/api-keys

# Secrets management
The `OPENAI_API_KEY` value is a secret intended to be used by authorized persons only.
The use of `crewai/summarizer/.env` file as kye placeholder is relevant for local tests.
Without this key, the building of Docker images can't take place.

For using a rutime key in the Github environment, a secret attached to the repository has to be defined 
in order a local .env file to be built with the assigned key.

Runtime key management is taken into account in the file `crewai/docker-compose.yaml` with instructions:
>     environment:
>      - OPENAI_API_KEY=${OPENAI_API_KEY}

And in workflow file` .github/workflows/build.yml ` with the followings instructions:
>
>       - name: Create .env file for summarizer
>        run: echo "OPENAI_API_KEY=${{ secrets.OPENAI_API_KEY }}" > summarizer/.env


Attaching a secret to the `crewai` repository is achieved from Github Actions as following
> 
> Github repository -> Settings -> Secrets and variables -> Actions
> 
> Click on "New repository secret"
> 
> Use `OPENAI_API_KEY` for secret name
> Assign the value retrieved from OpenAPI platform for API key.
> 
![img.png](doc/githubsecret.png)
> 

# Managing services
## Building services
> docker compose build
## Launching services
> docker compose up -d

## Stop services
> docker compose down

## Halting services
> docker compose down
For deleting containers without removing images 
## Managing a unique service
`cd .../crewai`

### Managing view service
> docker compose build view

> docker compose up -d view

> docker compose stop view

> docker compose down view
 
### Managing summarizer service
> docker compose build summarizer

> docker compose up -d summarizer

> docker compose stop summarizer

> docker compose down summarizer
# Tests
Once containers are launched and executed with Docker then file into `data/input.txt` may 
be used.

# The continuous integration workflow

# Result
The screen below shows the result of interactions between the two services. 
The left side is the original text.
The right side shows the result.
![img.png](doc/result.png)



# Github access
> https://github.com/dataforcast/crewAI