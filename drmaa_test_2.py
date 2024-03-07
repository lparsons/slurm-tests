#!/usr/bin/env python

import drmaa

def main():
    """
    Create a session, show that each session has an ID, use session ID to
    disconnect, then reconnect. Finally, exit.
    """
    s = drmaa.Session()
    s.initialize()
    print('A session was started successfully')
    response = s.contact
    print('session contact returns: %s' % response)
    s.exit()
    print('Exited from session')

    s.initialize(response)
    print('Session was restarted successfullly')
    s.exit()


if __name__=='__main__':
    main()


