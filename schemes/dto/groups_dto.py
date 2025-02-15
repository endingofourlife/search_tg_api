from pydantic import BaseModel


class GroupsDTO(BaseModel):
    url: str
    sub_count: int


