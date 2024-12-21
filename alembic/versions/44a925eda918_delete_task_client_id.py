"""delete task client id

Revision ID: 44a925eda918
Revises: ac7a4850baa8
Create Date: 2024-12-21 01:12:56.849640

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44a925eda918'
down_revision: Union[str, None] = 'ac7a4850baa8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Remover a chave estrangeira
    op.drop_constraint('ToDo_List_task_client_id_fkey', 'ToDo_List', type_='foreignkey')

    # Remover a coluna que depende da chave estrangeira
    op.drop_column('ToDo_List', 'task_client_id')

    # Agora, remover a tabela ToDo_Client
    op.drop_table('ToDo_Client')

def downgrade():
    # Recriar a tabela ToDo_Client
    op.create_table(
        'ToDo_Client',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )

    # Recriar a coluna na tabela ToDo_List
    op.add_column('ToDo_List', sa.Column('task_client_id', sa.Integer(), nullable=True))

    # Recriar a chave estrangeira
    op.create_foreign_key('ToDo_List_task_client_id_fkey', 'ToDo_List', 'ToDo_Client', ['task_client_id'], ['id'])