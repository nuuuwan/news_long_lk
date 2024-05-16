import os
import sys
from dataclasses import dataclass

import openai
from utils import JSONFile, Log, WWW, File

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


    def save(self):
        if not os.path.exists(self.dir_path):
            os.makedirs(self.dir_path)
        self.article_file.write(self.todict())
        log.info(f'Wrote {self.article_file.path}')



    def save_ai_summary(self):
        ai_summary_file = File(
            os.path.join(self.dir_path, 'ai_summary.txt')
        )
        if ai_summary_file.exists:
            log.debug(f'{ai_summary_file.path} exists')
            self.ai_summary = ai_summary_file.read()
            return

        openai_api_key = sys.argv[1]
        client = openai.Client(api_key=openai_api_key)

        system_cmd = "Summarize this article into a list of short bullets."
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

        ai_summary = response.choices[0].message.content
        ai_summary_file.write(ai_summary)
        log.info(f'Wrote {ai_summary_file.path}')
        self.ai_summary = ai_summary


    def save_ai_image(self):
        assert self.ai_summary
        ai_image_path = JSONFile(
            os.path.join(self.dir_path, 'ai_image.png')
        )
        if os.path.exists(ai_image_path.path):
            log.debug(f'{ai_image_path.path} exists')
            self.ai_image_path = ai_image_path
            return

        openai_api_key = sys.argv[1]
        client = openai.Client(api_key=openai_api_key)

        prompt = f'Generate an image without text to represent: {self.ai_summary}' 

        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )

        image_url = response.data[0].url
        log.debug(f'{image_url=}')
        
        WWW.download_binary(image_url, ai_image_path.path)
        log.info(f'Wrote {ai_image_path.path}')
        self.ai_image_path = ai_image_path

    def save_readme(self):
        assert self.ai_summary
        assert self.ai_image_path

        
        readme_file = JSONFile(os.path.join(self.dir_path, 'README.md'))
        lines = (
            [
                f'# {self.title}',
                '',
                f'![AI Image](ai_image.png)',
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
            + ['']
        )
        readme_file.write_lines(lines)
        log.info(f'Wrote {readme_file.path}')

    def save_all(self):
        self.save()
        self.save_ai_summary()
        self.save_ai_image()
        self.save_readme()
        