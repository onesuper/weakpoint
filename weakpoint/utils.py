


from os import path as op

def _cleanpath(*args):
    parts = [args[0].strip()]
    
    for arg in args[1:]:
        parts.append((arg.replace(op.sep, '', 1) if arg.startswith(op.sep) else arg).strip())
    
    return parts



def abspath(*args):
    return op.realpath(
        op.expanduser(
            op.join(
                *_cleanpath(*args)
            )
        )
    )


def normpath(*args):
    return op.normpath(
        op.join(
            *_cleanpath(*args)
        )
    )




