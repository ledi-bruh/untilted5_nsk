import markdown
import re


class MarkdownUploadFunc:

    async def __call__(self, md_data: str) -> str:
        html_data = markdown.markdown(md_data)
        data = re.sub('<[^>]*>', '', html_data)
        return data
