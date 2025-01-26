from .base_agent import BaseAgent

class SummarizerTool(BaseAgent):
    def __init__(self,max_retries,verbose = True):
        super.__init__(name="SummarizeTool",max_retries = max_retries,verbose = verbose)

    def execute(self,text):
        messages = [
            {
                "role":"System",
                "content":"You are an AI assistant that summarizes medical text as a slm agents."
            },
            {
                "role":"user",
                "content":(
                    "Please provide a concise summary of the following medical text:\n\n"
                    f"{text}\n\n summary:"
                )
            }

        ]
        summary = self.call_openai(messages,temperature=0.3,max_tokens=300)
        return summary
