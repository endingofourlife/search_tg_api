from pydantic import BaseModel


class CreateChannelRequest(BaseModel):
    url: str
    sub_count: int
    key_word: str

    def __str__(self):
        return f"CreateChannelRequest(url='{self.url}', sub_count={self.sub_count}, key_word='{self.key_word}')"

