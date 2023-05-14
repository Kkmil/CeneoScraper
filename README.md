# CeneoScraper

## Selektory CSS składowych opinii w serwisie ceneo

| Składowa | Nazwa | selektor |
| --- | --- | --- |
| Opinia | opinion/single opinion | div.js\_product-review |
| Identyfikator opinii | opinion\_id | [data-entry-id] |
| autor | author | span.user-post\_\_author-name |
| rekomendacja | recommendation | span.user-post\_\_author-recomendation \> em |
| liczba gwiazdek | score | span.user-post\_\_score-count |
| Czy opinia jest potwierdzona zakupem | purchased | div.review-pz |
| Data wystawienia opinii | opinion\_date | span.user-post\_\_published \> time:nth-child(1)[datetime] |
| Data zakupu produktu | purchase\_date | span.user-post\_\_published \> time:nth-child(2)[datetime] |
| Ile osób uznało opinię za przydatną | likes | button.vote-yes[data-total-vote]button.vote-yes \> spanspan[id^=votes-yes] |
| Ile osób uznało opinię za nieprzydatną | dislikes | button.vote-no[data-total-vote]button.vote-no \> spanspan[id^=votes-no] |
| Treść opinii | content | div.user-post\_\_text |
| lista wad | cons | div.review-feature\_\_title--negatives ~ div.review-feature\_\_item |
| lista zalet | pros | div.review-feature\_\_title--positives ~ div.review-feature\_\_item |