import os
import openai
from loguru import logger
from dotenv import load_dotenv
from abc import ABC,abstractmethod

load_dotenv()

openai.api_key = os.getenv("OPEN_API_KEY")

class BaseAgent(ABC):
    def __init__(self,name, max_retries = 2, verbose = True):
        self.name = name
        self.max_retries = max_retries
        self.verbose = verbose

    @abstractmethod
    def execute(self,*args,**kwargs):
        pass

    def call_openai(self,messages, temperature = 0.7,max_tokens = 150 ):
        retries = 0

        while retries < self.max_retries:
            try:
                if self.verbose:
                    logger.info(f"[{self.name}] sending message to openAi")
                    for msg in messages:
                        logger.debug(f"{msg['role']}: {msg['content']}")
                response = openai.chat.completetion.create(
                    model = "gpt-4o",
                    temperature = temperature,
                    max_tokens  = max_tokens
                )
                reply = response.choices[0].message

                if self.verbose:
                    logger.info(f"[{self.name} Received Response :{reply}]")
                return reply
            except Exception as e:
                retries += 1
                logger.error(f"[{self.name}] Error during opneAI call: {e}.Retry {retries}/{self.max_retries}")
        raise Exception(f"[{self.name}] Failed to get response from the openai after {self.max_retries} retries")

                                                           
        
