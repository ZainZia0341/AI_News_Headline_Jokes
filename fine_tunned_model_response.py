from langchain_community.llms import Bedrock
from langchain.prompts import PromptTemplate
import json

def deploy_and_test_model(model_name, prompt_text):
    # # Deploy the model
    # model_endpoint = Bedrock.create_endpoint(
    #     endpointName=f"{model_name}-endpoint",
    #     modelIdentifier=model_name
    # )
    # print(f"Model deployed at endpoint: {model_endpoint}")

    # Test the deployed model
    llm = Bedrock(
        model_id=model_name,
        model_kwargs={
            "maxTokenCount": 512,
            "stopSequences": [],
            "temperature": 1,
            "topP": 0.9
        }
    )

    prompt_template_name = PromptTemplate(
        input_variables=[prompt_text],
        template="You are a standup comedian who makes jokes on news headline take this news article content and make a humorous joke out of it and make sure the joke doesn't exceed more than 2 to 3 lines and make sure that the joke matches with the original news headline, here is the content, {prompt_text}"
    )

    rendered_prompt = prompt_template_name.format(prompt_text=prompt_text)
    response = llm.invoke(rendered_prompt)
    print("Test response: ", response)

# Test the model with an example prompt


example_prompt = '''

KEARNY, Ariz. (AP) — A wildfire burned down two structures and was threatening more than 50 others in the small desert community of Kearny, authorities said Wednesday.

The Simmons Fire, which broke out Tuesday, has burned 475 acres with zero containment, said Tiffany Davila, spokesperson for the Arizona Department of Forestry and Fire Management.

About 180 residents remained under mandatory evacuation in Kearny, which is located 75 miles (120 kilometers) north of Tucson and has a population of about 1,800.

Burning through dry fuels including grass and brush, the blaze was threatening a water treatment plant, copper mine, school district office and railroad line.

Pinal County officials said the town's Riverside neighborhood was evacuated Tuesday night, with a shelter opened at an elementary school.

Officials cut off electricity in northern Kearny for safety reasons, and four air tankers were fighting the fire along with crews on the ground.'''


model_name = 'fine_tunned_Titan_onAIJoke'
deploy_and_test_model(model_name, example_prompt)










