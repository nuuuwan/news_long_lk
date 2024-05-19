import os

from utils import File, JSONFile, Log, TimeFormat

log = Log('ArticleReadMe')


class ArticleReadMe:
    def save_readme(self):
        readme_file = JSONFile(os.path.join(self.dir_path, 'README.md'))
        lines = (
            [
                f'# {self.title}',
                '',
                '## Summary 🤖',
                '',
                self.ai_summary,
                '',
                '## Follow-up Questions 🤖',
                '',
                self.ai_follow_ups,
                '',
                '## Full Text',
                '',
                f'[{self.url}]({self.url})',
                '',
                f'*{self.time_str}*',
                '',
            ]
            + [paragraph + '\n' for paragraph in self.body_paragraphs]
            + [
                '',
            ]
        )
        readme_file.write_lines(lines)
        log.info(f'Wrote {readme_file.path}')

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
            lines.append(f'* `{article.source}` [{article.title}]({article.dir_path_unix})')
            prev_date_str = article.date_str
        readme_path = 'README.md'
        File(readme_path).write_lines(lines)
        log.info(f'Wrote {readme_path}')
