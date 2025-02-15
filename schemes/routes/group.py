from pydantic import BaseModel


class CreateGroupRequest(BaseModel):
    url: str
    sub_count: int
    key_word: str

    def __str__(self):
        return f"CreateGroupRequest(url='{self.url}', sub_count={self.sub_count}, key_word='{self.key_word}')"

