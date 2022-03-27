# API

Once the API is called by the client, we will validate and authorize the client and return information based on the level of access they have and information they required. The response will be in Json format by default.

There will be only one web service base URL be exposed and that particular url will have various paths and methods for clients to decide and call based on the data it requires.

## Web Service:

When the GUI client requires data from the service, the client will establish a connection to the Web API authorization service (Yet to be Implemented) to generate a jwt token and passing the user credentials. The request will be validated and on success issues an access and refresh token with expiry (expiry yet to be determined, usually 5 minutes). Expired access token can be refreshed using a refresh_token provided the session is still active. A user can Login from different IP address at the same time and will be issued different tokens for each login.

For audit purposes, the Web API will maintain an audit trail table for every request by logging user details, date & time, IP address, request and their downloaded record count.

The Web API will validate each user call against the user profile.

All requests except for the Authorization Endpoint must be decorated with an authorization header
“Authorization”:”Bearer {token from Authorization Endpoint}”
