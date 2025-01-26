from .base_agent import BaseAgent

class SanitizeDataValidatorTool(BaseAgent):
    def __init__(self,max_retries,verbose = True):
        super.__init__(name="SanitizeDataValidatorTool",max_retries = max_retries,verbose = verbose)

    def execute(self,original_data,sanitize_data):
        system_message =f"You are an expert ai agent which validates the sanitization of the medical data by checking the removal of the phi"
        user_content = (
            "Given a originla data and the sanitized data. verify that all the phi are removed.\n"
            "Providese a brief  analysis and rate the article on a scale of 1 to 5 , where 5 represents the excellent quality.\n\n"

            f"Original data :{original_data}\n\n"
            f"Santization data : \n{sanitize_data}\n\n"
            "Validation:"
        )
       

        message = [
           {"role":"System","content":system_message},
           {"role":"user","content":user_content}
        ]
        validation= self.call_openai(message,temperature=0.3,max_tokens=300)
        return validation