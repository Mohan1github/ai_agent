from .base_agent import BaseAgent

class DatasanitizerTool(BaseAgent):
    def __init__(self,max_retries,verbose = True):
        super.__init__(name="DatasanitizerTool",max_retries = max_retries,verbose = verbose)

    def execute(self,medical_data):
        messages = [
            {
                "role":"System",
                "content":"You are an AI assistant that sanitize medical data by removing Protected Health Infomration (PHI)."
            },
            {
                "role":"user",
                "content":(
                    "Remove all PHI from the following data:\n\n"
                    f"{medical_data}\n\n summary:"
                )
            }

        ]
        sanitized = self.call_openai(messages,max_tokens=300)
        return sanitized
