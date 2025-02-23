"""initial setup

Revision ID: f8ebeb454bc4
Revises: 
Create Date: 2025-02-12 16:42:43.706191

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f8ebeb454bc4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('channels',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('sub_count', sa.INTEGER(), nullable=False),
    sa.Column('key_word', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('groups',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('sub_count', sa.INTEGER(), nullable=False),
    sa.Column('key_word', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('groups')
    op.drop_table('channels')
    # ### end Alembic commands ###
