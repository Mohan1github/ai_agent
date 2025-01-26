from .base_agent import BaseAgent

class SummaruArticleValidatorTool(BaseAgent):
    def __init__(self,max_retries,verbose = True):
        super.__init__(name="SummaryArticleValidatorTool",max_retries = max_retries,verbose = verbose)

    def execute(self,original_text,summary):
        system_message =f"You are an expert ai agent which validates the given summary comparing with the orignal text"
        user_content = (
            "Given a original text and summary. Assess the summary for its correctness and its standards.\n"
            "Providese a brief  analysis and rate the summary with the original text on a scale of 1 to 5 , where 5 represents the excellent quality.\n\n"

            f"Original text :{original_text}\n\n"
            f"Summary : \n{summary}\n\n"
            "Validation:"
        )
       

        message = [
           {"role":"System","content":system_message},
           {"role":"user","content":user_content}
        ]
        validation= self.call_openai(message,temperature=0.3,max_tokens=300)
        return validation