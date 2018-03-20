from networktables import NetworkTables

# NetworkTables.initialize(server='205.154.151.73')
table = NetworkTables.getTable('taco')
# table.putNumber('yes', 857)
table.putNumber('testy', 19.5)

# print(table.getNumber('thingy2'))