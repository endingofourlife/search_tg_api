from pydantic import BaseModel


class ChannelsDTO(BaseModel):
    url: str
    sub_count: int


