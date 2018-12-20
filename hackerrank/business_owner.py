import fileinput

# from Yelp
'''
42
1 42 1
42 1 1
2 42 2
88 2 1
'''

class Message:
    def __init__(self, sender, recipient, conversation_id):
        self.sender = sender
        self.recipient = recipient
        self.conversation_id = conversation_id


def business_responsiveness_rate(biz_owner_id, all_messages):
    # TODO: COMPLETE ME
    total_response = set()
    total_conversation = set()
    for message in all_messages:
        if message.recipient == biz_owner_id:
            total_conversation.add(message.conversation_id)
        elif message.sender == biz_owner_id:
            total_response.add(message.conversation_id)

    if len(total_response):
        return int(len(total_response) / len(total_conversation) * 100)

    return 0


if __name__ == '__main__':

    lines = list(fileinput.input())
    biz_owner_id = lines[0].rstrip()

    all_messages = []
    for line in lines[1:]:
        if not line:
            break
        sender, recipient, conversation_id = line.split(' ')
        all_messages.append(
            Message(
                sender,
                recipient,
                conversation_id.rstrip(),
            ),
        )

    print(business_responsiveness_rate(biz_owner_id, all_messages))
