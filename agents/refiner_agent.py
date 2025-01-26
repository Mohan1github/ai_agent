from .base_agent import BaseAgent

class RefinerTool(BaseAgent):
    def __init__(self,max_retries,verbose = True):
        super.__init__(name="RefinerTool",max_retries = max_retries,verbose = verbose)

    def execute(self,topic , outline = None):
        messages = [
            {
                "role":"System",
                "content":
                [
                    {
                        "type":"text",
                        "text":"you are an expert ai agent who refines and enhances the articles for clarity , integrity , coherence and academic purpose"
                    }
                ]
            },
            {
                "role":"user",
                "content":
                [
                    {
                        "type":"text",
                        "text":"Please refine the  articles for clarity , integrity , coherence and academic purpose"
                    }
                ]
            }

        ]
        refined = self.call_openai(messages,temperature= 0.3,max_tokens=300)
        return refined