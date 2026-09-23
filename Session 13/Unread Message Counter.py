def count_unread_messages(messages):
    total=messages.get("count",0)

    for subgroup in messages.get("subgroups",[]):
        total+=count_unread_messages(subgroup)

    return total

messages={"count":5,"subgroups":[{"count":3,"subgroups":[{"count":2},{"count":4}]},
                                 {"count":6,"subgroups":[{"count":1}]}]}

print("Total Unread Messages : ",count_unread_messages(messages))
