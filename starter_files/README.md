# Operationalizing Machine Learning

In this project I was tasked with creating, training and deploying an automl model. I setup the endpoint to have authorization and tested the deployed automl model by making requests via a python script. I also created and published a pipeline that could do all of the steps of creating and automl model. Lastly, I used a rest endpoint to interact with the published pipeline.

## Architectural Diagram
![](./diagrams/project_arch.png)

## Key Steps
* AutoMl Experiment
  1. Uploaded bank marketing dataset
    ![](../screenshots/bank_marketing_dataset.png)
  1. Setup and run an AutoML experiment with bank marketing dataset<br/>
    Completed Run
    ![](../screenshots/automl_run_completed.png)
    Best Model
    ![](../screenshots/automl_best_model.png)
  1. Deploy the best model from the experiment with authentication then test with [logs.py](./logs.py)<br/>
    Application Insights Enabled Endpoint with [enable_ai.py](./enable_ai.py):
    ![](../screenshots/ai_enable_automl_model_endpoint.png)
    Output from logs.py
    ![](../screenshots/automl_logs_script.png)
  1. Download and run swagger on localhost
    ![](../screenshots/automl_swagger.png)
  1. Consume model endpoints with [endpoints.py](./endpoint.py)
    ![](../screenshots/endpoint_result.png)
  1. (Optional) Benchmark Endpoint
    ![](../screenshots/benchmark.png)

* Pipeline
    1. Create pipeline from provided [jupyter notebook](./aml-pipelines-with-automated-machine-learning-step.ipynb)
    ![](../screenshots/pipeline_created.png)
    Bank marketing set with pipeline
    ![](../screenshots/bankmarketing_with_automl.png)
    1. Publish Pipeline
    ![](../screenshots/published_pipeline_endpoint.png)
    1. Use Published pipeline<br/>
    Run details from pipeline in progress
    ![](../screenshots/run_details_in_progress.png)
    Run details from pipeline completed
    ![](../screenshots/run_details_complete.png)
    Scheduled fruns from using published pipeline
    ![](../screenshots/scheduled_runs.png)

## Screen Recording

[Screenrecording](https://youtu.be/OecewP26IAc)
