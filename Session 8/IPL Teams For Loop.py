def long_name(teams):

    for team in teams:
        if len(team)<=6:
            continue
        print(team)

ipl_teams=["Mumbai Indians","Chennai Super Kings","Delhi Capitals","Rajasthan Royals","Punjab Kings"]

long_name(ipl_teams)
