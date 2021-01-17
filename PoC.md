# PoC

## partendo dagli IP utilizzati

1. chiedi all'utente quale subnet desidera (/29, /30, ...)
1. apri il file con gli IP utilizzati
1. considera il primo IP
1. considera la subnet in cui quell'IP è incluso
1. crea una lista con gli IP di quella subnet (compresa network e broadcast)
1. fai un match tra quell'ip e quella lista
1. se il numero di match è 1, quell'ip è interessante

## partendo dagli IP liberi

1. apri il file con gli IP in lettura
1. prendi il primo ip libero
1. considera la subnet in cui e' incluso
1. metti i 4 (o 8) ip di quella subnet in una lista
1. fai un match tra la lista di cui sopra, e gli ip liberi
1. se la lunghezza del match e' 3 (o 7), hai trovato un ip interessante

## Altra idea...

1. apri il file con gli IP in lettura
1. sortalo
1. ricava tutte le /24
1. per ogni network, ricava tutte le /30 o /29 (potrebbe essere il terzo argomento)
1. fai una roba del genere:
```
>>> for addr in IPv4Network('192.0.2.0/28'):
...     addr
...
IPv4Address('192.0.2.0')
IPv4Address('192.0.2.1')
IPv4Address('192.0.2.2')
IPv4Address('192.0.2.3')
IPv4Address('192.0.2.4')
IPv4Address('192.0.2.5')
IPv4Address('192.0.2.6')
IPv4Address('192.0.2.7')
IPv4Address('192.0.2.8')
IPv4Address('192.0.2.9')
IPv4Address('192.0.2.10')
IPv4Address('192.0.2.11')
IPv4Address('192.0.2.12')
IPv4Address('192.0.2.13')
IPv4Address('192.0.2.14')
IPv4Address('192.0.2.15')
```
