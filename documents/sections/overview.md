# ssdcs-design

## Overview

Safe Repository will be a solution to store experimental data. It will offer REST APIs to manipulate resources and consume events from a Message Broker.

There will be two kinds of resources: users, experiments, and measurements.

### Users

Users will represent the users authorized to interact with the solution. There will be two user types: administrators and scientists with the following role matrix:

TBD

### Experiments

Experiments will represent single experiments. Only administrators and scientists associated with the experiment will have access to an experiment.

### Data

Raw data from the measurements. It will be a read-only resource associated with an experiment displaying the measurements collected from the Message Broker.
