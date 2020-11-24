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

<table>
<caption>Addlink</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Metoda API</p></td>
<td><p>Metoda SDK</p></td>
</tr>
<tr class="even">
<td><p>Draft</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Images</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Add</p></td>
<td><p>?</p></td>
</tr>
</tbody>
</table>

<table>
<caption>Entries</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Metoda API</p></td>
<td><p>Metoda SDK</p></td>
</tr>
<tr class="even">
<td><p>Stream</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Hot</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Active</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Observed</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Entry</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Add</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Edit</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>VoteUp</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>VoteRemove</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Upvoters</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Delete</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Comment</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>CommentAdd</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>CommentEdit</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>CommentDelete</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>CommentVoteUp</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>CommentVoteRemove</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>ObservedComments</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Favorite</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>SurveyVote</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>CommentFavorite</p></td>
<td><p>?</p></td>
</tr>
</tbody>
</table>

<table>
<caption>Hits</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Metoda API</p></td>
<td><p>Metoda SDK</p></td>
</tr>
<tr class="even">
<td><p>Popular</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Day</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Week</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Month</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Year</p></td>
<td><p>?</p></td>
</tr>
</tbody>
</table>

<table>
<caption>Links</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Metoda API</p></td>
<td><p>Metoda SDK</p></td>
</tr>
<tr class="even">
<td><p>Promoted</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Upcoming</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Observed</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Link</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>VoteUp</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>VoteRemove</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>VoteDown</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Upvoters</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Downvoters</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Top</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Comments</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>CommentVoteUp</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>CommentVoteDown</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>CommentVoteCancel</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>CommentAdd</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>CommentEdit</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>CommentDelete</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Comment</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Related</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>RelatedAdd</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>RelatedVoteUp</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>RelatedVoteDown</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Favorite</p></td>
<td><p>?</p></td>
</tr>
</tbody>
</table>

<table>
<caption>Login</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Metoda API</p></td>
<td><p>Metoda SDK</p></td>
</tr>
<tr class="even">
<td><p>Index</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Connect</p></td>
<td><p>?</p></td>
</tr>
</tbody>
</table>

<table>
<caption>Mywykop</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Metoda API</p></td>
<td><p>Metoda SDK</p></td>
</tr>
<tr class="even">
<td><p>Index</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Tags</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Users</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Entries</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Links</p></td>
<td><p>?</p></td>
</tr>
</tbody>
</table>

<table>
<caption>Notifications</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Metoda API</p></td>
<td><p>Metoda SDK</p></td>
</tr>
<tr class="even">
<td><p>Index</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Count</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>HashTags</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>HashTagsCount</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Total</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>TotalCount</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>ReadAllNotifications</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>ReadDirectedNotifications</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>ReadHashTagsNotifications</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>MarkAsRead</p></td>
<td><p>?</p></td>
</tr>
</tbody>
</table>

<table>
<caption>PM</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Metoda API</p></td>
<td><p>Metoda SDK</p></td>
</tr>
<tr class="even">
<td><p>ConversationsList</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Conversation</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>SendMessage</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>DeleteConversation</p></td>
<td><p>?</p></td>
</tr>
</tbody>
</table>

<table>
<caption>Profiles</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Metoda API</p></td>
<td><p>Metoda SDK</p></td>
</tr>
<tr class="even">
<td><p>Index</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Actions</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Added</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Commented</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Comments</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Published</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Entries</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>CommentedEntries</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>EntriesComments</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Related</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Followers</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Followed</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Badges</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Digged</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Buried</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Rank</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Observe</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>UnObserve</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Block</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>UnBlock</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>AvailableColors</p></td>
<td><p>?</p></td>
</tr>
</tbody>
</table>

<table>
<caption>Search</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Metoda API</p></td>
<td><p>Metoda SDK</p></td>
</tr>
<tr class="even">
<td><p>Links</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Entries</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Profiles</p></td>
<td><p>?</p></td>
</tr>
</tbody>
</table>

<table>
<caption>Search</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Metoda API</p></td>
<td><p>Metoda SDK</p></td>
</tr>
<tr class="even">
<td><p>Links</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Entries</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Profiles</p></td>
<td><p>?</p></td>
</tr>
</tbody>
</table>

<table>
<caption>Settings</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Metoda API</p></td>
<td><p>Metoda SDK</p></td>
</tr>
<tr class="even">
<td><p>Profile</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Avatar</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Background</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Password</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>ResetPassword</p></td>
<td><p>?</p></td>
</tr>
</tbody>
</table>

<table>
<caption>Suggest</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Metoda API</p></td>
<td><p>Metoda SDK</p></td>
</tr>
<tr class="even">
<td><p>Tags</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Users</p></td>
<td><p>?</p></td>
</tr>
</tbody>
</table>

<table>
<caption>Tags</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Metoda API</p></td>
<td><p>Metoda SDK</p></td>
</tr>
<tr class="even">
<td><p>Index</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Links</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Entries</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Observe</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Unobserve</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Notify</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Dontnotify</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Block</p></td>
<td><p>?</p></td>
</tr>
<tr class="even">
<td><p>Unblock</p></td>
<td><p>?</p></td>
</tr>
</tbody>
</table>

<table>
<caption>Terms</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Metoda API</p></td>
<td><p>Metoda SDK</p></td>
</tr>
<tr class="even">
<td><p>Index</p></td>
<td><p>?</p></td>
</tr>
<tr class="odd">
<td><p>Confirm</p></td>
<td><p>?</p></td>
</tr>
</tbody>
</table>
