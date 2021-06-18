from fastapi import Request


def db_session(request: Request):
    return request.state.db_session
