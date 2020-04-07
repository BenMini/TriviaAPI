from app import app, setup_db
from app.models import Question, Category


@app.shell_context_processor
def make_shell_context():
    return {'db': setup_db, 'Question': Question, 'Category': Category}
