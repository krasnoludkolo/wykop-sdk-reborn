## 0.6.0

* ujednolicenie wszystkich metod do formatu `zasób_metoda`[#42](https://github.com/krasnoludkolo/wykop-sdk-reborn/issues/42)

## 0.5.0

* dodanie możliwości logowania za pomocą loginu i hasła [#47](https://github.com/krasnoludkolo/wykop-sdk-reborn/issues/47)

## 0.4.0

* usunięcie parametru `password` 
* **[BETA]** dodanie nowego klienta będącego rozszerzeniem bazowego klienta o możliwość używania kilku kluczy api
  [#25](https://github.com/krasnoludkolo/wykop-sdk-reborn/issues/25)

## 0.3.0

* metoda `search_entries`, `search_profiles`, `search_links` [#15](https://github.com/krasnoludkolo/wykop-sdk-reborn/issues/15)
* przedrostek `entry_` dla wszystkich metod związanych z komentarzami do wpisów na mirkoblogu
* zmiana nazewnictwa metod związanych z powiadomieniami, tak aby wszystkie miały przedrostek `notification_`/`notifications_`

## 0.2.3

* naprawa błedu pobierania konkretnego wpisu na mikroblogu

## 0.2.2

* naprawa błędu logowania

## 0.2.1

* dodawanie obrazków do nowych wpisów i komentarzy [#28](https://github.com/krasnoludkolo/wykop-sdk-reborn/issues/28)
* dodawanie obrazków do edytowanych wpisów i komentarzy [#28](https://github.com/krasnoludkolo/wykop-sdk-reborn/issues/28)
* poprawny request zwraca pole `data` [#27](https://github.com/krasnoludkolo/wykop-sdk-reborn/issues/27)

## 0.2.0

* usunięcie przedrostka `get_`
* obsługa wiadomości prywatnych
* obsługa mikrobloga (bez wstawiania obrazków oraz ankiet)
