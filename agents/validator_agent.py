from .base_agent import BaseAgent

class Validator_agent(BaseAgent):
    def __init__(self,max_retries,verbose=True):
        super.__init__(name="Validator_agent",max_retries = max_retries,verbose = verbose)

    def execute(self):

        system_promt = f" You are an expert AI system validates each and every request to the llm are processed completely."

        user_content = f"  Given an instruction with the option selected on the drop down menu in the streamlit ui make sure that the request and process is perfectly delivered."

        messages = [


            {
                "role":"system","content":system_promt
            },
            {
                "role":"user","content":user_content
            }
        ]

        validation_result = self.call_openai(messages,temperature=0.3,max_tokens=300)
        return validation_result