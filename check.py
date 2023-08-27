from P4 import P4, P4Exception  # Import the module


def check(port) -> bool:
    p4 = P4()  # Create the P4 instance
    p4.port = port

    try:
        p4.connect()
        p4.run("trust", "-y")
        info = p4.run("info")
        print(info)
        p4.disconnect()
        return True
    except P4Exception as p4e:
        print(p4e)
        for e in p4.errors:
            print("Perforce error: ", e)
        return False
    except Exception as e:
        print(e)
        return False
