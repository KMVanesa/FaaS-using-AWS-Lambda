# Function as a Service

## Build and Deploy instructions for web application on AWS EC2 instance .
Install code deployment agent via AMI on the instance on which deployment is to performed.

Create code deployment group and code deploy application and attach them to the code deployment agent.

Setup a Github project on project to trigger the deployment of Web Application and Lambda Function on AWS.

## Steps to perform for CI and CD

Step-1:- Build the AMI for the instance.
```bash
curl -u <secret key of circleci> \ -d build_parameters[CIRCLE_JOB]=build \ <link to the Github AMI repository> 
```

step-2: Build the Infrastructure via Terraform 
```bash
terraform apply
```

step-3:- After applying Terraform, deploy the WebApp to AWS via Circle CI API
```bash
curl -u <secret key of circleci> \ -d build_parameters[CIRCLE_JOB]=build \ <link to the Github Webapp repository>
```

step-4:- Build lambda function as a service using Circle CI API
```bash
curl -u <secret key of circleci> \ -d build_parameters[CIRCLE_JOB]=build \ <link to the Github FAAS repository>
``` 