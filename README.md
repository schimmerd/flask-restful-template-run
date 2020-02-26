# Example README

[Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

This repository contains the source code of the Google Cloud Run Service ...

1. PROD
    - PROJECT_ID = ""
    - CLOUD_SOURCE_REPOSITORY = ""
    - CLOUD_BUILD_TRIGGER = ""
    - CONTAINER_IMAGE_NAME = 
    - CLOUD_RUN_SERVICE = ""
2. DEV
    - ...


## How to use the API

This is a general architecture of the ...

[Architecture Overview]

The API is callable under the following URL: $URL

- `VERSION="v1"`
- `API_ENDPOINT(s)= ...`
- `API_URI=$URL/$VERSION/$API`

#### /example

- Method: GET / POST
- Description: ...

POST Request like:

``
{
    ...
}
``

Output: 

``
{
    ...
}
``

## Development
### 1. Code Structure

The service based on the Python3 Flask RESTful Framework. The Flask app is created in the app.py file.

```
api.add_resource(Example, "/v1/apis/example", resource_class_args=(logger,))
```

There is a options.py class which gets instanciated at startup - within the class the parameters for the different environments get setted.
The Environment gets setted wihtin the two cloudbuild files -> here is an os env variable 'RUN_MODE' is setted. The Dockerfile creates the Docker image for the container.

### 2. Deployment

What is Cloud Run?

Cloud Run is a service by Google Cloud Platform to run your stateless HTTP containers without worrying about provisioning machines, clusters or autoscaling.
With Cloud Run, you go from a "container image" to a fully managed web application running on a domain name with TLS certificate that auto-scales with requests in a single command. You only pay while a request is handled.

[More Q&A here](https://github.com/ahmetb/cloud-run-faq)

Cloud Run configuration
- [Configuring Memory Limit](https://cloud.google.com/run/docs/configuring/memory-limits)
- [Configuring Concurrency](https://cloud.google.com/run/docs/configuring/concurrency)
    - [Concurrency concept](https://cloud.google.com/run/docs/about-concurrency)
- [Configuring Request timeout](https://cloud.google.com/run/docs/configuring/request-timeout)

#### 2.1. Manual

```
gcloud builds submit --tag gcr.io/${PROJECT_ID}/${SERVICE_NAME}
gcloud run deploy --image gcr.io/${PROJECT_ID}/${SERVICE_NAME} --platform managed --region europe-west4 --concurrency=10
```

#### 2.2. Create Cloud Build Trigger

1. Create cloudbuild.yaml (specifiy service-name: ...)
2. IAM "...@cloudbuild.gserviceaccount.com" needs Cloud Run Admin and Service Account user rights
3. Create Cloud Build Trigger on Repository

After that, every push to master (or other specific branch or tag) creates a new version of the Cloud Run service

For more information see https://cloud.google.com/run/docs/continuous-deployment

In our case we're working with two different environments PROD and DEV. Therefore we created two different cloudbuild.yaml files for each environment. The service is deployed on the DEV or PROD project depending on the branch it gets checked in. Everything checked into the dev* branch gets deployed to the DEV project.
bsp: 
- Push to master -> Deployment to PROD
- Push to - anything which contains - 'dev*' in branch --> Deployment to DEV

### Additional Information
- Version: ...
- Links: ...

-------------
Dominik Schimmer - 26.02.2020