"""create posts Table

Revision ID: b5f09bc69347
Revises: 
Create Date: 2024-09-17 04:10:16.247813

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b5f09bc69347'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',sa.Column('id',sa.Integer,nullable=False,primary_key=True),sa.Column('title',sa.String,nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
