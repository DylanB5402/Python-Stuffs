from networktables import NetworkTables
# table = NetworkTables.initialize(server = '2600:1700:c5b0:5670:d032:a017:86e3:cee0')
# NetworkTables.setClientMode()
table = NetworkTables.getTable('taco')
# NetworkTables.setPort(11)
food = table.putNumber('thingy2', 254)
print(table.getNumber('testy'))
# NetworkTables.getPath()
