from .base_agent import BaseAgent

class WriteArticleValidatorTool(BaseAgent):
    def __init__(self,max_retries,verbose = True):
        super.__init__(name="WriteArticleValidatorTool",max_retries = max_retries,verbose = verbose)

    def execute(self,topic ,article, outline = None):
        system_message =f"You are an expert ai agent which validates the article written by the llms."
        user_content = (
            "Given a topic and an article. Assess the article for its correctness and its standards.\n"
            "Providese a brief  analysis and rate the article on a scale of 1 to 5 , where 5 represents the excellent quality.\n\n"

            f"Topic :{topic}\n\n"
            f"Article : \n{article}\n\n"
            "Validation:"
        )
       

        message = [
           {"role":"System","content":system_message},
           {"role":"user","content":user_content}
        ]
        validation= self.call_openai(message,temperature=0.3,max_tokens=300)
        return validation