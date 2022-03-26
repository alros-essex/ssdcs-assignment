# Overview

"Safe Repository" will be a solution to store streams of experimental data for the Hadron Collider at CERN and make them available to scientists. The data will be delivered to the solution in the form of messages from a Message Broker. Data will be made available through a REST interface. There will be three resources: users, experiments, and measurements.

## Users

Users will represent the users authorized to interact with the solution. There will be two user types: administrators and scientists with the following role matrix:

*Administrators*
| resource      | scope    | access |
|---------------|----------|--------|
| users         | complete | RW     |
| experiments   | complete | RW     |
| measurements  | complete | R      |

*Scientists*
| resource      | scope                                           | access |
|---------------|-------------------------------------------------|--------|
| users         | user's record                                   | RW     |
| experiments   | only records associated with user               | RW     |
| measurements  | only records associated with user's experiments | R      |

## Experiments

Experiments will represent single experiments. Only administrators and scientists associated with the experiment will have access to an experiment.

## Data

Raw data from the measurements. It will be a read-only resource associated with an experiment displaying the measurements collected from the Message Broker.
