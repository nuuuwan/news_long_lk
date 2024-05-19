import sys

import openai
from utils import Log

log = Log('OpenAICommon')


class OpenAICommon:
    @staticmethod
    def get_client():
        openai_api_key = sys.argv[1]
        log.debug('openai_api_key=' + openai_api_key[:12] + '***')
        return openai.Client(api_key=openai_api_key)
