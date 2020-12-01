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

api = wykop.WykopAPI(key, secret, accountkey=account_key)
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

## Stan implementacji metod api

### Addlink

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Draft|:x:|
|Images|:x:|
|Add|:x:|

### Entries

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Stream|`stream_entries`|
|Hot|`hot_entries`|
|Active|:x:|
|Observed|:x:|
|Entry|`entry`|
|Add|:x:|
|Edit|:x:|
|VoteUp|:x:|
|VoteRemove|:x:|
|Upvoters|:x:|
|Delete|:x:|
|Comment|:x:|
|CommentAdd|:x:|
|CommentEdit|:x:|
|CommentDelete|:x:|
|CommentVoteUp|:x:|
|CommentVoteRemove|:x:|
|ObservedComments|:x:|
|Favorite|:x:|
|SurveyVote|:x:|
|CommentFavorite|:x:|

### Hits

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Popular|`hits_popular`|
|Day|:x:|
|Week|:x:|
|Month|`hits_month`|
|Year|:x:|

### Links

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Promoted|`links_promoted`|
|Upcoming|:x:|
|Observed|:x:|
|Link|:x:|
|VoteUp|:x:|
|VoteRemove|:x:|
|VoteDown|:x:|
|Upvoters|:x:|
|Downvoters|:x:|
|Top|:x:|
|Comments|:x:|
|CommentVoteUp|:x:|
|CommentVoteDown|:x:|
|CommentVoteCancel|:x:|
|CommentAdd|:x:|
|CommentEdit|:x:|
|CommentDelete|:x:|
|Comment|:x:|
|Related|:x:|
|RelatedAdd|:x:|
|RelatedVoteUp|:x:|
|RelatedVoteDown|:x:|
|Favorite|:x:|

### Login
|||
|--- |--- |
|Metoda API|Metoda SDK|
|Index|:x:|
|Connect|:x:|

### Mywykop

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Index|:x:|
|Tags|:x:|
|Users|:x:|
|Entries|:x:|
|Links|:x:|

### Notifications

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Index|`direct_notifications`|
|Count|`direct_notifications_count`|
|HashTags|`hashtags_notifications`|
|HashTagsCount|`hashtags_notifications_count`|
|Total|`all_notifications`|
|TotalCount|`all_notifications_count`|
|ReadAllNotifications|`mark_all_notification_as_read`|
|ReadDirectedNotifications|`mark_all_direct_notification_as_read`|
|ReadHashTagsNotifications|`mark_all_hashtag_notification_as_read`|
|MarkAsRead|`mark_notification_as_read`|

### PM

|||
|--- |--- |
|Metoda API|Metoda SDK|
|ConversationsList|`conversations_list`|
|Conversation|`conversation`|
|SendMessage|`send_message`|
|DeleteConversation|:x:|

### Profiles

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Index|:x:|
|Actions|:x:|
|Added|:x:|
|Commented|:x:|
|Comments|:x:|
|Published|:x:|
|Entries|:x:|
|CommentedEntries|:x:|
|EntriesComments|:x:|
|Related|:x:|
|Followers|:x:|
|Followed|:x:|
|Badges|:x:|
|Digged|:x:|
|Buried|:x:|
|Rank|:x:|
|Observe|`observe_profile`|
|UnObserve|`unobserve_profile`|
|Block|`block_profile`|
|UnBlock|`unblock_profile`|
|AvailableColors|:x:|

### Search

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Links|:x:|
|Entries|:x:|
|Profiles|:x:|

### Settings 

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Profile|:x:|
|Avatar|:x:|
|Background|:x:|
|Password|:x:|
|ResetPassword|:x:|

### Suggest

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Tags|:x:|
|Users|:x:|

### Tags

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Index|`tag`|
|Links|`tag_links`|
|Entries|`tag_entries`|
|Observe|`observe_tag`|
|Unobserve|`unobserve_tag`|
|Notify|`enable_tags_notifications`|
|Dontnotify|`disable_tags_notifications`|
|Block|`block_tag`|
|Unblock|`unblock_tag`|

### Terms

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Index|:x:|
|Confirm|:x:|
