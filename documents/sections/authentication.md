# Authentication

An authentication endpoint will validate credentials comparing the input with the hashes stored in the database. The endpoint will return a JSON web token that will remain valid for a limited time. The token will be required in the calls to all other APIs.
The authentication endpoint will require the inclusion of a shared secret (API key) in the request. This additional measure will limit the chances to perform a brute force attack.

# Authorization

Authorization will be handled at the level of the storage. Whenever a user will perform a query, his identity will be part of the query.

For example:

```sql
SELECT d.* from user_experiments ue, data d
where d.experiment_id = :experiment_id -- clause to select the data
and ue.experiment_id = d.experiment_id -- join
and ue.user_id = :user_id              -- safety measure
```

If the id of the current user is not associated with the experiment, the result of the query will be empty thanks to the last two lines.
