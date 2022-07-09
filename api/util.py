from flask import jsonify
from sqlalchemy.exc import SQLAlchemyError
import traceback



def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except (AssertionError, KeyError, ValueError) as err:
            res = jsonify({
                'ex': str(type(err)),
                'status': 'error',
                'error': str(err),
                'stacktrace': traceback.format_exc()
            })
            res.status_code = 400
            return res
        except SQLAlchemyError as err:
            err = str(err.__dict__.get('orig') or err)
            res = jsonify({'ex': str(type(err)), 'status': 'error', 'error': err})
            res.status_code = 400
            return res
        except Exception as err:
            res = jsonify({'ex': str(type(err)), 'status': 'error', 'error': str(err)})
            res.status_code = 500
            return res
    wrapper.__name__ = func.__name__
    return wrapper


