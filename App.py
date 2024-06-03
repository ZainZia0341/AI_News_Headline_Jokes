from langchain_community.llms import Bedrock
from langchain.prompts import PromptTemplate
import json

def get_llm_body(prompt_text):
    prompt_template_name = PromptTemplate(
    input_variables = [prompt_text],
    template = "You are a standup comedian who creates short jokes based on news headlines. Given the following news article content, generate a humorous joke that is exactly 2 to 3 lines long and relevant to the original headline. Here is the content: {prompt_text}"
)
    
    rendered_prompt = prompt_template_name.format(prompt_text=prompt_text)

    model_kwargs = {
            "maxTokenCount": 512,
            "stopSequences": [],
            "temperature": 1,
            "topP": 0.9
    }

    llm = Bedrock( #create a Bedrock llm client
        model_id="amazon.titan-text-express-v1", #use the requested model
        model_kwargs = model_kwargs
    )

    response = llm.invoke(rendered_prompt)
    response = json.dumps(response)
    # print("response ", response)
    return response


