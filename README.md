Fork biblioteki [wykop-sdk](https://github.com/p1c2u/wykop-sdk) w której
staram się poprawiać sdk wraz z (nie)udokumentowanymi zmianami w api
wykopu.

Lista zmian:

-   Usunięcie parametru `login` i `password` z metod logujących przez
    api (potrzebny jest jedynie account\_key)

-   Usunięcie klienta v1

-   rozdzielenie `named params` i `api params`

-   metody PM:

    -   Conversation

    -   SendMessage

-   medoty notifications:

    -   MarkAsRead

Stan implementacji metod api

### Addlink

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Draft|?|
|Images|?|
|Add|?|

### Entries

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Stream|?|
|Hot|?|
|Active|?|
|Observed|?|
|Entry|?|
|Add|?|
|Edit|?|
|VoteUp|?|
|VoteRemove|?|
|Upvoters|?|
|Delete|?|
|Comment|?|
|CommentAdd|?|
|CommentEdit|?|
|CommentDelete|?|
|CommentVoteUp|?|
|CommentVoteRemove|?|
|ObservedComments|?|
|Favorite|?|
|SurveyVote|?|
|CommentFavorite|?|

### Hits

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Popular|?|
|Day|?|
|Week|?|
|Month|?|
|Year|?|

### Links

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Promoted|?|
|Upcoming|?|
|Observed|?|
|Link|?|
|VoteUp|?|
|VoteRemove|?|
|VoteDown|?|
|Upvoters|?|
|Downvoters|?|
|Top|?|
|Comments|?|
|CommentVoteUp|?|
|CommentVoteDown|?|
|CommentVoteCancel|?|
|CommentAdd|?|
|CommentEdit|?|
|CommentDelete|?|
|Comment|?|
|Related|?|
|RelatedAdd|?|
|RelatedVoteUp|?|
|RelatedVoteDown|?|
|Favorite|?|

### Login
|||
|--- |--- |
|Metoda API|Metoda SDK|
|Index|?|
|Connect|?|

### Mywykop

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Index|?|
|Tags|?|
|Users|?|
|Entries|?|
|Links|?|

### Notifications

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Index|?|
|Count|?|
|HashTags|?|
|HashTagsCount|?|
|Total|?|
|TotalCount|?|
|ReadAllNotifications|?|
|ReadDirectedNotifications|?|
|ReadHashTagsNotifications|?|
|MarkAsRead|?|

### PM

|||
|--- |--- |
|Metoda API|Metoda SDK|
|ConversationsList|?|
|Conversation|?|
|SendMessage|?|
|DeleteConversation|?|

### Profiles

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Index|?|
|Actions|?|
|Added|?|
|Commented|?|
|Comments|?|
|Published|?|
|Entries|?|
|CommentedEntries|?|
|EntriesComments|?|
|Related|?|
|Followers|?|
|Followed|?|
|Badges|?|
|Digged|?|
|Buried|?|
|Rank|?|
|Observe|?|
|UnObserve|?|
|Block|?|
|UnBlock|?|
|AvailableColors|?|

### Search

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Links|?|
|Entries|?|
|Profiles|?|

### Settings 

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Profile|?|
|Avatar|?|
|Background|?|
|Password|?|
|ResetPassword|?|

### Suggest

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Tags|?|
|Users|?|

### Tags

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Index|?|
|Links|?|
|Entries|?|
|Observe|?|
|Unobserve|?|
|Notify|?|
|Dontnotify|?|
|Block|?|
|Unblock|?|

### Terms

|||
|--- |--- |
|Metoda API|Metoda SDK|
|Index|?|
|Confirm|?|
