# Dimensioning the system

## Disk

User and experiment data will require less than 1Kb per record, and their number is expected to be in the range of thousands. Therefore it is safe to assume that a few megabytes will be sufficient to store them.

Each measurement is expected to require at least 22 bytes.

* 2 bytes per measurement type
* 8 bytes per timestamp
* 4 bytes per experiment id
* 8 bytes per measure

With 1 million measures per experiment, each experiment will require about 21Mb of space.

## CPU and memory

TBD
