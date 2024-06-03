import boto3
import json
import s3_creation

bedrock = boto3.client('bedrock')

job_name = 'fine-tuning-AI-Jokes-again-again-again-again7'
model_name = 'fine_tunned_Titan_onAIJoke'
role_arn = 'arn:aws:iam::654654320621:role/AIJOKESIAMROLE'

base_model_id = "amazon.titan-text-express-v1"

# Create model customization job
response = bedrock.create_model_customization_job(
    customizationType="FINE_TUNING",
    jobName=job_name,
    customModelName=model_name,
    roleArn=role_arn,
    baseModelIdentifier=base_model_id,
    hyperParameters={
        "epochCount": "10",
        "batchSize": "1",
        "learningRate": "0.00001",
    },
    trainingDataConfig={"s3Uri": s3_creation.s3_creation_url()},
    outputDataConfig={"s3Uri": "s3://aijokes/output"},
)

print("Model customization job created:", response)



# # Get model customization job status
# response = bedrock.describe_model_customization_job(
#     jobName=job_name
# )

# while response["modelCustomizationJobStatus"] == "IN_PROGRESS":
#     print("Model customization job still in progress...")
#     response = bedrock.describe_model_customization_job(
#         jobName=job_name
#     )

# if response["modelCustomizationJobStatus"] == "COMPLETED":
#     print("Model customization job completed successfully!")
#     print("Model ARN:", response["modelCustomizationJobOutput"]["modelArn"])
# else:
#     print("Model customization job failed!")
#     print("Error message:", response["modelCustomizationJobErrorMessage"])

# # Fine-tune the model
# response = bedrock.start_model_customization_job(
#     jobName=job_name
# )

# while response["modelCustomizationJobStatus"] == "IN_PROGRESS":
#     print("Model customization job still in progress...")
#     response = bedrock.describe_model_customization_job(
#         jobName=job_name
#     )

# if response["modelCustomizationJobStatus"] == "COMPLETED":
#     print("Model customization job completed successfully!")
#     print("Model ARN:", response["modelCustomizationJobOutput"]["modelArn"])
# else:
#     print("Model customization job failed!")
#     print("Error message:", response["modelCustomizationJobErrorMessage"])

# # Get the model
# response = bedrock.describe_model(
#     modelName=model_name
# )

# print("Model details:", response)

# # # Get the model predictions
# # response = bedrock.predict_with_model(
# #     inputData={"instances": json.dumps(["This is a joke."])},
# #     modelName=model_name
# # )

# # print("Predicted output:", response)

# # # Delete the model
# # response = bedrock.delete_model(
# #     modelName=model_name
# #     )