# APIs

Once the API is called by the client, the solution will validate and authorize the client and return information based on the level of access they have and information they required. The response will be in Json format by default.

There will be only one web service base URL be exposed and that particular url will have various paths and methods for clients to decide and call based on the data it require.

## Web Service:

When the GUI client requires data from the service, the client will establish a connection to the Web API authorization service (Yet to be Implemented) to generate a jwt token and passing the user credentials. The Web API will check the credentials and will issue “Access token” and “Refresh token” in the response as JSON value. These access token will be then used in the subsequent API method calls from the client. The Access token will have issue time and Expire time (expiry yet to be determined, usually 5 minutes). Once the token is about to be expired, the client has to provide the refresh token and get a new token. A user can Login from different IP address at the same time and will be issued different tokens for each login.

For audit purposes, the Web API will maintain an audit trail table for every request by logging user details, date & time, IP address, request and their downloaded record count.

The Web API will validate each user call against the user profile.
