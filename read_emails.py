from simplegmail import Gmail
from simplegmail.query import construct_query

gmail = Gmail()

query_params = {
    "newer_than": (90, "day"),
}

messages = gmail.get_messages(query=construct_query(query_params))

if not messages:
    print("Couldn't find any emails.")
else:
    for message in messages:
        print("To: " + message.recipient)
        print("From: " + message.sender)
        print("Subject: " + message.subject)
        print("Date: " + message.date)
        print("Preview: " + message.snippet)
        print("------------------------------------------------------------------")
        
        """
        with open("email_samples.txt", "a") as f:
            if message.plain:
                if len(message.plain) < 1000:
                    f.write(message.plain)
        """