from functools import cached_property

from utils import File, Log

from news.core import Article
from utils_future import OpenAICommon

log = Log('NewsLetter')

# Not used
class NewsLetter:
    MODEL = 'gpt-4'
    MAX_ARTICLES = 30

    @cached_property
    def summary_content(self):
        articles = Article.list_all()
        if len(articles) > self.MAX_ARTICLES:
            articles = articles[: self.MAX_ARTICLES]
        n_articles = len(articles)
        log.debug(f'Building NewsLetter from {n_articles} articles')
        lines = []
        for article in articles:
            lines.append(article.title)
            lines.append(article.readme_path_unix)
            lines.append(article.ai_summary)
            lines.append('...')
        content = '\n\n'.join(lines)
        return content

    @cached_property
    def newsletter_content(self):
        client = OpenAICommon.get_client()
        system_cmd = (
            'Aggregate the following articles into a newsletter,'
            + ' clearly including links, group by topic: '
        )
        try:
            response = client.chat.completions.create(
                model=self.MODEL,
                messages=[
                    {"role": "system", "content": system_cmd},
                    {
                        "role": "user",
                        "content": self.summary_content,
                    },
                ],
            )
        except BaseException as e:
            log.error(f'Failed to summarize {self.url}: {str(e)}')
            return ''

        return response.choices[0].message.content

    def build(self):
        newsletter_path = 'README.newsletter.md'
        File(newsletter_path).write_lines(
            ['# Newsletter', '', self.newsletter_content, '']
        )
        log.info(f'Wrote {newsletter_path}')
