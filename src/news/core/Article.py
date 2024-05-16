import os
import sys
from dataclasses import dataclass
from functools import cached_property

import openai
from utils import WWW, File, JSONFile, Log, Time, TimeFormat

from news.core.ArticleHead import ArticleHead

log = Log('Article')


@dataclass
class Article(ArticleHead):
    DIR_DATA = os.path.join('data', 'articles')

    time_str: str
    ut: int
    body_paragraphs: list[str]

    def todict(self):
        return dict(
            url=self.url,
            date_id=self.date_id,
            title=self.title,
            #
            time_str=self.time_str,
            ut=self.ut,
            body_paragraphs=self.body_paragraphs,
        )

    @property
    def date_str(self):
        return TimeFormat.DATE.format(Time(self.ut))

    @property
    def dir_path_unix(self):
        return self.dir_path.replace('\\', '/')

    @staticmethod
    def from_dict(d):
        return Article(
            url=d['url'],
            date_id=d['date_id'],
            title=d['title'],
            #
            time_str=d['time_str'],
            ut=d['ut'],
            body_paragraphs=d['body_paragraphs'],
        )

    @staticmethod
    def from_file(article_file):
        d = article_file.read()
        return Article.from_dict(d)

    @staticmethod
    def list_all():
        articles = []
        for child_dir in os.listdir(Article.DIR_DATA):
            article_file = JSONFile(
                os.path.join(Article.DIR_DATA, child_dir, 'article.json')
            )
            if article_file.exists:
                article = Article.from_file(article_file)
                articles.append(article)
        articles.sort(
            key=lambda article: article.ut,
            reverse=True,
        )
        log.debug(f'Found {len(articles)} articles')
        return articles

    def save(self):
        if not os.path.exists(self.dir_path):
            os.makedirs(self.dir_path)
        self.article_file.write(self.todict())
        log.info(f'Wrote {self.article_file.path}')

    @cached_property
    def ai_summary(self):
        ai_summary_file = File(os.path.join(self.dir_path, 'ai_summary.txt'))
        if ai_summary_file.exists:
            return ai_summary_file.read()

        openai_api_key = sys.argv[1]
        client = openai.Client(api_key=openai_api_key)

        system_cmd = "Summarize the following article:"
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": system_cmd},
                    {
                        "role": "user",
                        "content": '\n\n'.join(self.body_paragraphs),
                    },
                ],
            )
        except BaseException:
            log.error(f'Failed to summarize {self.url}')
            return ''

        ai_summary = response.choices[0].message.content
        ai_summary_file.write(ai_summary)
        log.info(f'Wrote {ai_summary_file.path}')
        return ai_summary

    @cached_property
    def ai_image_path(self):
        ai_image_path = JSONFile(os.path.join(self.dir_path, 'ai_image.png'))
        if os.path.exists(ai_image_path.path):
            return ai_image_path

        openai_api_key = sys.argv[1]
        client = openai.Client(api_key=openai_api_key)

        prompt = f'Generate a painting titled "{self.title} in Sri Lanka"'

        try:
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
        except BaseException:
            log.error(f'Failed to generate image for {self.url}')
            return None

        image_url = response.data[0].url
        log.debug(f'{image_url=}')

        WWW.download_binary(image_url, ai_image_path.path)
        log.info(f'Wrote {ai_image_path.path}')
        return ai_image_path

    def save_readme(self):
        readme_file = JSONFile(os.path.join(self.dir_path, 'README.md'))
        lines = (
            [
                f'# {self.title}',
                '',
                '## AI Generated Summary',
                '',
                self.ai_summary,
                '',
                '## Original Text',
                '',
                f'[{self.url}]({self.url})',
                '',
                f'*{self.time_str}*',
                '',
            ]
            + [paragraph + '\n' for paragraph in self.body_paragraphs]
            + [
                '',
                '![AI Image](ai_image.png)',
                '',
            ]
        )
        readme_file.write_lines(lines)
        log.info(f'Wrote {readme_file.path}')

    def save_all(self):
        self.save()
        self.ai_summary
        self.ai_image_path
        self.save_readme()

    @staticmethod
    def build_readme():
        articles = Article.list_all()
        lines = [
            '# Sri Lankan News :sri_lanka:',
            '',
            '*Long-Form Articles & Opinions*',
        ]
        prev_date_str = None
        for article in articles:
            if prev_date_str != article.date_str:
                lines.extend(['', f'## {article.date_str}', ''])
            lines.append(f'* [{article.title}]({article.dir_path_unix})')
            prev_date_str = article.date_str
        readme_path = 'README.md'
        File(readme_path).write_lines(lines)
        log.info(f'Wrote {readme_path}')
