from Trace import StackTrace

strace = StackTrace().trace

def test_strace():
    print strace("tada!")

test_strace()
