def method_not_support_msg(o, name=None):
    if name is None:
        name = "Unknown method"
    return f"{name} does not support {type(o)}"
