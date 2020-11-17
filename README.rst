Fork biblioteki `wykop-sdk`_ w której staram się poprawiać sdk wraz z (nie)udokumentowanymi zmianami w api wykopu.

.. _wykop-sdk: https://github.com/p1c2u/wykop-sdk

Lista zmian:

- Usunięcie parametru `login` i `password` z metod logujących przez api (potrzebny jest jedynie account_key)
- Usunięcie klienta v1
- rozdzielenie `named params` i `api params`
- metody PM:
    - Conversation
    - SendMessage