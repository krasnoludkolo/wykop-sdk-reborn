# Wykop API v2 Python SDK
[![PyPI version](https://badge.fury.io/py/wykop-sdk-reborn.svg)](https://badge.fury.io/py/wykop-sdk-reborn)

Biblioteka ta jest implementacją [Wykop API v2](https://www.wykop.pl/dla-programistow/apiv2docs/wstep/) w Python.


Fork [wykop-sdk](https://github.com/p1c2u/wykop-sdk) w którym staram się poprawiać sdk wraz z (nie)udokumentowanymi zmianami w api
wykopu.

## Instalacja

`pip install wykop-sdk-reborn`

## Uwierzytelnienie
Aby móc wykonywać działania jako zalogowany użytkownik należy się wcześniej uwierzytenić. 
Potrzebne do tego będą klucze aplikacji, oraz klucz "połączenie" które można wygenerować [tutaj](https://www.wykop.pl/dla-programistow/apiv2/)
  
```python
import wykop

api = wykop.WykopAPI(klucz_aplikacji, sekret_aplikacji)
api.authenticate(klucz_polaczenia)
api.conversations_list()

# lub

api = wykop.WykopAPI(key, secret, account_key=account_key)
api.authenticate()
api.conversations_list()
```

## Jak pomóc?

* Masz pomysł albo chcesz zgłosić błąd?

Zgłoś w zakładce [issues](https://github.com/krasnoludkolo/wykop-sdk-reborn/issues)

* Chcesz pomóc w rozwoju?

Wybierz jakieś zadanie z [issues](https://github.com/krasnoludkolo/wykop-sdk-reborn/issues), 
napisz komentarz ze chcesz się nim zając i mnie oznacz. Zrób forka repo, opracuj rozwiązanie i wystaw RPa

## Zgłaszanie błędów

[issues](https://github.com/krasnoludkolo/wykop-sdk-reborn/issues) albo napisz mi PW na wykopie [@krasnoludkolo](https://www.wykop.pl/ludzie/krasnoludkolo/)

## Dokumentacja metod
To, jakim metodom api odpowiają jakie metody klienta można sprawdzić na [wiki](https://github.com/krasnoludkolo/wykop-sdk-reborn/wiki/Stan-implementacji-metod).