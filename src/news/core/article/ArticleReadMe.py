import os

from utils import File, JSONFile, Log, TimeFormat

log = Log('ArticleReadMe')


class ArticleReadMe:
    @property
    def readme_path(self):
        return os.path.join(self.dir_path, 'README.md')

    @property
    def readme_path_unix(self):
        return self.readme_path.replace('\\', '/')

    def save_readme(self):
        readme_file = JSONFile(self.readme_path)
        lines = (
            [
                f'# {self.title}',
                '',
                f'[{self.url}]({self.url})',
                '',
                f'*{self.time_str_formatted}*',
                '',
            ]
            + [paragraph + '\n' for paragraph in self.body_paragraphs]
            + [
                '',
            ]
        )
        readme_file.write_lines(lines)
        log.debug(f'Wrote {readme_file.path}')

    @classmethod
    def build_readme(cls):
        articles = cls.list_all()
        last_updated_str = TimeFormat.TIME.formatNow
        lines = [
            '# Sri Lankan News :sri_lanka:',
            '',
            '*Long-Form Articles & Opinions*',
            '',
            f'Last Updated **{last_updated_str}**',
        ]
        prev_date_str = None
        for article in articles:
            if prev_date_str != article.date_str:
                lines.extend(['', f'## {article.date_str}', ''])
            lines.append(
                f'* [{article.title}]({article.readme_path_unix})'
                + f' `{article.source}`'
            )
            prev_date_str = article.date_str
        readme_path = 'README.md'
        File(readme_path).write_lines(lines)
        log.debug(f'Wrote {readme_path}')
