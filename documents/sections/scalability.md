# Scalability

## Periodic pressure on resources

All components of the solution will be stateless and allow for horizontal scalability.  Clustering solutions such as Kubernetes have autoscale functionality to regulate the number of running instances and deal with variable demand. Autoscale functions are also efficient to contain the costs since additional CPUs and memory are allocated and billed only when required.

## Interactive response requirements between request and reply

TBD

## Substantial data download requirements

It is expected an elevated flow of data coming from queues while users will visualize them almost in real-time. The database will act as a buffer between the component responsible for storing the incoming data and the component responsible to make it available to the users. It is expected that the highest pressure could come from the input flow. Since reading a large amount of data could put pressure on the database, queries should be paginated.
