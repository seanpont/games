
def assert_equal(expected, actual, message=''):
    if actual != expected:
        if not message:
            message = "Expected %s but got %s" % (expected, actual)
        raise Exception(message)


