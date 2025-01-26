from .base_agent import BaseAgent

class WriteArticleTool(BaseAgent):
    def __init__(self,max_retries,verbose = True):
        super.__init__(name="WriteArticleTool",max_retries = max_retries,verbose = verbose)

    def execute(self,topic , outline = None):
        system_message =f"You are an expert academic writer"
        user_content = f"write a research article about the following topic:\n Topic:{topic} \n\n"

        if outline:
            user_content += f"Outline:\n {outline}\n\n"
        user_content+=f"Article:\n"

        message = [
           {"role":"System","content":system_message},
           {"role":"user","content":user_content}
        ]
        article = self.call_openai(message,temperature=0.3,max_tokens=300)
        return article