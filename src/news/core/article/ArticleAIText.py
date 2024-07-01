import os
from functools import cached_property

from utils import File, Log

from utils_future import OpenAICommon

log = Log('ArticleAIText')


class ArticleAIText:
    MODEL = 'gpt-4'

    def get_generic_ai_text(self, cmd_type, system_cmd):
        ai_text_path = File(os.path.join(self.dir_path, f'ai_{cmd_type}.txt'))
        if ai_text_path.exists:
            return ai_text_path.read()

        client = OpenAICommon.get_client()

        try:
            response = client.chat.completions.create(
                model=self.MODEL,
                messages=[
                    {"role": "system", "content": system_cmd},
                    {
                        "role": "user",
                        "content": '\n\n'.join(self.body_paragraphs),
                    },
                ],
            )
        except BaseException as e:
            log.error(f'Failed to summarize {self.url}: {str(e)}')
            return ''

        ai_text = response.choices[0].message.content
        ai_text_path.write(ai_text)
        log.debug(f'🤖 Wrote {ai_text_path.path}')
        return ai_text

    @cached_property
    def ai_summary(self):
        return self.get_generic_ai_text(
            'summary',
            "Summarize the following article into 10 bullets. Annotate with emojis.",
        )

