import tbapy

def sheet():
    tba = tbapy.TBA('kOvjIfPTsNCSlHfA1MIzwrnAg7Os1aNEAMNXLAaj1ohzjAEHKUrTfkb1h0r4VfFc')
    # team_list = tba.event_teams('2017cc', 2017)
    # for x in range(1, len(team_list)):
    print(tba.team_events(254, 2017, True))        
        # print(tba.team_awards(team_list[x]), 2017)
        # x+=1
    # print(tba.events(2017))

sheet()