"""alterações no env.py

Revision ID: 1a40c2c95c49
Revises: 44a925eda918
Create Date: 2025-01-16 22:40:01.948087

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a40c2c95c49'
down_revision: Union[str, None] = '44a925eda918'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('ToDo_List', sa.Column('new_column', sa.String(50), nullable=True))

def downgrade() -> None:
    op.drop_column('ToDo_List', 'new_column')

