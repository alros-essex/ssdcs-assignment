# ssdcs-design

## Components

![components](components.png)

[diagram source](components.drawio)

The solution comprises multiple components responsible for different aspects.

### Safe Repository

Safe Repository is the core component responsible for storing the Handron Collider's experimental data. It exposes multiple endpoints to configure the application resources and can process parallel data streams through input queues. The application stores the information on an external database.

### Storage

A database is responsible for the storage of the data. (TBD encryption)

### HTTP Input

An HTTP proxy is responsible for encrypting the communications with the solution, offloading the incoming encryption, and adding encryption to the output. All HTTP-based communication will flow through the proxy.

### Data Streams

An MQ Broker will expose queues to accept data streams. (TBD encryption)

### Logging and Monitoring

(TBD, possibly ELK Stack?)

### Deployment

The entire solution will be containerized with Docker and orchestrated with Docker Compose. This choice makes it easier to deploy the solution in other platforms such as Kubernetes with minimal changes to the configuration.
