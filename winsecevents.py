# Author: Craig Ferguson
# 01/09/2024
# script to pull data from the Windows Security logs. Must be run as Administrator

import win32evtlog  # You'll need the pywin32 package. Install it using pip: pip install pywin32
import win32evtlogutil
import win32con

def get_security_events(server=None):
    """
    Retrieve security events from the Windows Security log.

    Args:
    - server (str): Optional parameter to specify the server name. If None, uses local machine.

    Returns:
    - list: List of security events.
    """
    events = []

    # Connect to the Event Log
    hand = win32evtlog.OpenEventLog(server, "Security")

    # Get the total number of records in the log
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    total = win32evtlog.GetNumberOfEventLogRecords(hand)

    # Retrieve events
    while True:
        events_list = win32evtlog.ReadEventLog(hand, flags, 0)
        if not events_list:
            break

        for event in events_list:
            # Filter for security events (Event ID 528 is a sample, you can change based on your requirement)
            if event.EventID == 4624:
                events.append(event)

    # Close the Event Log
    win32evtlog.CloseEventLog(hand)

    return events

def main():
    # Fetch security events
    security_events = get_security_events()

    # Display some information from the events
    for event in security_events:
        print(f"Event ID: {event.EventID}")
        print(f"Time Generated: {event.TimeGenerated}")
        print(f"Message: {win32evtlogutil.SafeFormatMessage(event, 'Security')}")
        print("-" * 50)

if __name__ == "__main__":
    main()