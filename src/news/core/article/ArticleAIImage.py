import os
from dataclasses import dataclass
from functools import cached_property

from utils import WWW, JSONFile, Log

from utils_future import OpenAICommon

log = Log('ArticleAIImage')


@dataclass
class ArticleAIImage:
    IMAGE_MODEL = "dall-e-3"
    IMAGE_SIZE = "1024x1024"
    IMAGE_QUALITY = "standard"
    IMAGE_N = 1

    @cached_property
    def ai_image_path(self):
        ai_image_path = JSONFile(os.path.join(self.dir_path, 'ai_image.png'))
        if os.path.exists(ai_image_path.path):
            return ai_image_path

        client = OpenAICommon.get_client()

        prompt = (
            'Generate a painting, in a genre of your choosing, '
            + f'titled "{self.title}" in a Sri Lankan context.'
        )

        try:
            response = client.images.generate(
                model=self.IMAGE_MODEL,
                prompt=prompt,
                size=self.IMAGE_SIZE,
                quality=self.IMAGE_QUALITY,
                n=self.IMAGE_N,
            )
        except BaseException:
            log.error(f'Failed to generate image for {self.url}')
            return None

        image_url = response.data[0].url
        log.debug(f'{image_url=}')

        WWW.download_binary(image_url, ai_image_path.path)
        log.info(f'🤖 Wrote {ai_image_path.path}')
        return ai_image_path
