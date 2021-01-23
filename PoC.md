# PoC

## partendo dagli IP utilizzati

1. chiedi all'utente quale subnet desidera (/29, /30, ...)
1. apri il file con gli IP utilizzati
1. considera il primo IP
1. considera la subnet in cui quell'IP è incluso
1. crea una lista con gli IP di quella subnet (compresa network e broadcast)
1. fai un match tra quell'ip e quella lista
1. se il numero di match è 1, quell'ip è interessante
