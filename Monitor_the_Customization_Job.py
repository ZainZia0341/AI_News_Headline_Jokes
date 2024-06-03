import time
import boto3
bedrock = boto3.client('bedrock')

# def monitor_customization_job(job_name):
#     bedrock = boto3.client('bedrock')
    
#     while True:
#         response = bedrock.describe_model_customization_job(jobName=job_name)
#         job_status = response['status']
#         print(f"Job status: {job_status}")
        
#         if job_status in ['COMPLETED', 'FAILED']:
#             return response
        
#         time.sleep(60)  # Wait for a minute before checking again

# job_name = 'fine-tuning-AI-Jokes-again-again-again-again7'
# response = monitor_customization_job(job_name)

# if response['status'] == 'COMPLETED':
#     print("Model customization job completed successfully")
# else:
#     print("Model customization job failed:", response)


status = bedrock.get_model_customization_job(jobIdentifier="fine-tuning-AI-Jokes-again-again-again-again7")["status"]

print("status checking ", status)