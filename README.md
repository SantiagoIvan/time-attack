# time-attack
Pequeño script en Python de un time attack contra un server  para hallar usuarios existentes

La idea es tirar una secuencia de POST contra el server. Suponiendo que el backend esta escrito medio malardo, si un usuario no existe,
va a devolver "User or password incorrect!"
En cambio si el usuario es correcto, la idea es que tire ese mismo error, pero con un poco mas de retraso. 
En este caso, este script lo hice para resolver un Desafio en TryHackMe. Los POST con usuarios incorrectos tardaban aproximadamente 0.6 segs
mientras que si un usuario existía, tardaba un segundo mas
