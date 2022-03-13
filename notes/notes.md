# ssdcs-design

Some initial notes to draft the work to do, feel free to edit!

We need to design an application with these characteristics:
* CRUD: a webservice is probably a good idea. Once we set up the basics we just have to define at least two resources and create 4 APIs with GET, POST, PUT, and DELETE for each one. For example for Hadron Collider the resources could be "scientists", "experiments" and "measurements" with a 1-to-many relationship between them.
* an eye on GDPR: if the APIs let the user retrieve/update/delete his own data, we should be covered
* security measures:
  * authentication: we need an API that gives a token, the token must have a duration, and be included in all calls to the resources
  * authorisation: anything to block user A when he tries to access user B’s stuff
  * data encryption: we can encrypt data in the storage and the data in output. The latter maybe requires a node in front of the webapp
  * event monitoring: essentially, logging of everything except for secrets. Yes to “user X logged in”, No to “user X logged with pass xyz”
* microservice:
  * scalability: I suppose they mean dockerize the application and being able to run multiple instances. Docker should be easy to add at the end. To run multiple instances we have to deal with the user's session.
  * distributed session: it's hard to do and avoided. A common solution is to delegate the authentication (but not the authorization) to a frontend node so the service can be stateless.
* two events occurring: I assume that this is to demonstrate that we built something thread-safe. We can setup some script to fire multiple calls at the same time to demo it.


To be included
* local or remote access: if it's a webservice, it's also remote
* magnitude of storage required: size of one record times the number of expected records per user times the number of users + some margin
* CPU capacity: we can describe how it works in a cloud provider such as AWS
* the roles of users who are accessing the system: what about users + admin
* concurrent data streams: an example about the API calls
* encryption algorithm(s): copy&paste of what we pick for the storage and the frontend node
* approach to data storage: to avoid concurrency issues, a database is probably the best choice. Storing the logs with Docker requires additional ifrastructure (to be looked up)
* design pattern(s): this will come easy after the first draft
* cybersecurity: we can play with [STRIDE](https://en.wikipedia.org/wiki/STRIDE_%28security%29) after we design the APIs. It's fairly simple.
* UML:
  * sequence diagram: for example the flow authentication - API call
  * class diagram: a draft of how we will structure the software
  * activity diagram: in the example of the Handron Collider, it can be "creation of scientists" followed by "creation of experiment", some updates, then "creation of data"...
