## 0.9.4

* dodanie metod z grupy `profiles` (`EntriesComments`)

## 0.9.3

* dodanie metod z grupy `mywykop` (`entries`)

## 0.9.2

* dodanie metody z grupy `links` (`link`)

## 0.9.1

* dodanie metod z grupy `profile` (`profile_comments`, `profile_entries`)

## 0.9.0

* dodanie pierwszych metod z grupy `profile` (`profile_added`, `profile_buried`, `profile_digged`)

## 0.8.2

* obsługa błędu api, które zwraca status 503 jeśli nie istnieje konwersacja [#68](https://github.com/krasnoludkolo/wykop-sdk-reborn/issues/68)


## 0.8.0

* dodanie `wykop connect` [#63](https://github.com/krasnoludkolo/wykop-sdk-reborn/issues/63)

## 0.7.0

* dodanie metod `settings` [#16](https://github.com/krasnoludkolo/wykop-sdk-reborn/issues/16)
* dodanie dedykowanego wyjątek dla sytuacji, gdy zostanie wysłana wiadomość do osoby, która ma zablokowane pw [#43](https://github.com/krasnoludkolo/wykop-sdk-reborn/issues/43)
* dodanie możliwości filtrowania wyniku pobieranie notyfikacji według typu [#37](https://github.com/krasnoludkolo/wykop-sdk-reborn/issues/37)
* wewnętrzny refactoring `requestor`a tak, aby nie wysyłał jeśli parametr jest ustawiony na None [#54](https://github.com/krasnoludkolo/wykop-sdk-reborn/issues/54)

## 0.6.1

* `entries_stream` oraz `entries_hot` nie ignorują parametru page [#53](https://github.com/krasnoludkolo/wykop-sdk-reborn/issues/53)


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
