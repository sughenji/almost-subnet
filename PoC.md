# PoC

## partendo dagli IP utilizzati

1. chiedi all'utente quale subnet desidera (/29, /30, ...)
1. apri il file con gli IP utilizzati
1. per ogni IP, ricava la network di appartenenza
1. crea una lista di networks
1. per ogni network, fai un match con il file degli IP utilizzati
1. se il numero di match è 1, quell'ip è interessante
