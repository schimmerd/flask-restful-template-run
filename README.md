# Flask Template for Google Cloud Run 

Code and deploy very fast and easily based on Google Cloud resources

## Development
### 1. Code Structure

The service based on the Python3 Flask RESTful Framework. The Flask app is created in the app.py file.

```
api.add_resource(Example, "/v1/apis/example", resource_class_args=(logger,))
```
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
gcloud builds submit --tag gcr.io/$PROJECT_ID/$SERVICE_NAME
gcloud run deploy --image gcr.io/$PROJECT_ID/$SERVICE_NAME --platform managed --region europe-west1 --concurrency 10 --memory 2Gi --allow-unauthenticated
```

#### 2.2. Create Cloud Build Trigger

1. Create cloudbuild.yaml (specifiy service-name: ...)
2. IAM "...@cloudbuild.gserviceaccount.com" needs Cloud Run Admin and Service Account user rights
3. Create Cloud Build Trigger on Repository

After that, every push to master (or other specific branch or tag) creates a new version of the Cloud Run service

For more information see https://cloud.google.com/run/docs/continuous-deployment

<hr />

Dominik Schimmer - 26.02.2020