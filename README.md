# ETL Job ML Model Deployment
Code to deploy an ML model inside a batch job

This code is used in this [blog post](https://medium.com/@brianschmidt_78145/a-batch-job-ml-model-deployment-da41b8ea5a99).

## Installation 
The makefile included with this project contains targets that help to automate several tasks.

To download the source code execute this command:
```bash
git clone https://github.com/schmidtbri/etl-job-ml-model-deployment
```
Then create a virtual environment and activate it:
```bash

# go into the project directory
cd etl-job-ml-model-deployment

make venv

source venv/bin/activate
```

Install the dependencies:
```bash
make dependencies
```

## Running the unit tests
To run the unit test suite execute these commands:
```bash

# first install the test dependencies
make test-dependencies

# run the test suite
make test
```
