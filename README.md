# Työhaku

## Sovelluksen Toiminnot

* Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
* Käyttäjä pystyy lisäämään ja poistamaan omia työpaikkailmoituksia.
* Käyttäjä näkee sovellukseen lisätyt työpaikkailmoitukset.
* Käyttäjä pystyy etsimään työpaikkailmotuksia hakusanalla.
* Sovelluksessa on käyttäjäsivu, jotka näyttävät tilastoja ja käyttäjän lisäämät julkaisut.
* Käyttäjä pystyy valitsemaan julkaisulle yhden tai useamman luokittelun.
* Käyttäjä pystyy hakemaan toisen käyttäjän julkaisemaa työpaikkaa.
* Käyttäjä pystyy poistamaan oman hakemuksensa.
* Työpaikka ilmoituksen julkaisija näkee listan käyttäjistä jotka ovat hakeneet työpaikkaa ja heidän lähettämänsä hakemukset.


## Sovelluksen asennus

 Asenna `flask`- kirjasto:

 ```
 $ pip install flask
 ```

 Luo tietokannan taulut ja lisää alkutiedot:

```
$ sqlite3 database.db < schema.sql
$ sqlite3 database.db < init.sql
```

Käynnistä Sovellus:

```
$ flask run
```
