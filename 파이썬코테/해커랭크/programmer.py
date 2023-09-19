import heapq

def getMinRooms(meetingTimings):
    meetingTimings.sort()
    meeting_rooms = [meetingTimings[0][1]]
    for meeting in meetingTimings[1:]:
        if meeting_rooms[0] > meeting[0]:
            heapq.heappush(meeting_rooms, meeting[1])
        else:
            heapq.heapreplace(meeting_rooms, meeting[1])
    return len(meeting_rooms)