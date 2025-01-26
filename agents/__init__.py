from .summarizer_tool import SummarizerTool
from .refiner_agent import RefinerTool
from .sanitize_data import DatasanitizerTool
from .sanitize_data_validator import SanitizeDataValidatorTool
from .writearticle import WriteArticleTool
from .write_article_validator import WriteArticleValidatorTool
from .summary_validator_agent import SummaruArticleValidatorTool
from .validator_agent import Validator_agent

class AgentManager:
    def __init__(self,max_retries = 2,verbose = True):
        self.agent = {
        "Summarize": SummarizerTool(max_retries=max_retries,verbose=verbose),
        "Write_article": WriteArticleTool(max_retries=max_retries,verbose=verbose),
        "sanitizer_tool": SanitizeDataValidatorTool(max_retries=max_retries,verbose = verbose),
        "summary_validator":SummaruArticleValidatorTool(max_retries=max_retries,verbose=verbose),
        "Refiner_tool": RefinerTool(max_retries=max_retries,verbose = verbose),
        "sanitizer_data_validator_tool": SanitizeDataValidatorTool(max_retries=max_retries,verbose= verbose),
        "Writer_article_validator_tool": WriteArticleValidatorTool(max_retries=max_retries,verbose=verbose),
        "Data_sanitizer_toll": DatasanitizerTool(max_retries=max_retries,verbose=verbose),
        "Validator_agent_tool":Validator_agent(max_retries=max_retries,verbose = verbose)
        }

    
    def get_agent(self,agent_name):
        agent = self.agent.get(agent_name)
        if not agent:
            raise ValueError(f" Agent '{agent_name}' not found!")
        return agent
    
        