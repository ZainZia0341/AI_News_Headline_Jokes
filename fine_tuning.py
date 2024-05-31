import boto3
import json
import s3_creation

bedrock = boto3.client('bedrock')

job_name = 'fine-tuning-AI-Jokes-again-again-again-again2443334'
model_name = 'fine_tunned_Titan_onAIJoke'
role_arn = 'arn:aws:iam::654654320621:role/AIJOKESIAMROLE'

base_model_id = "amazon.titan-text-express-v1"

# Create model customization job
response = bedrock.create_model_customization_job(
    customizationType="CONTINUED_PRE_TRAINING",
    jobName=job_name,
    customModelName=model_name,
    roleArn=role_arn,
    baseModelIdentifier=base_model_id,
    hyperParameters={
        "epochCount": "10",
        "batchSize": "8",
        "learningRate": "0.00001",
    },
    trainingDataConfig={"s3Uri": s3_creation.s3_creation_url()},
    outputDataConfig={"s3Uri": "s3://aijokes/output"},
)

print("Model customization job created:", response)
