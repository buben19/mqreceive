# mqreceive changelog

## v0.1.0

 - Initial version.
 - Code taken from mqspeak project.
 - Implemented `Broker` class.
 - Declared `DataCollector` class interface.
 - Implemented `DataIdentifier` class.
 - Receiving:
   - Implemented `BrokerThreadManager` class for receiving MQTT updates from multiple brokers.
   - Implemented `BrokerReceiver` class for simple receiving data from single MQTT broker.
   - Implemented meaningful MQTT client IDs.
