# Apache-Kafka
This repository demonstrate how the apache kafka generally works.<br /><hr>
First set up the <b>zookeeper</b> and then the <b>kafka server</b>, next to manage kafka clusters use <b>CMAK</b>: https://github.com/yahoo/CMAK <br />
I've used an API(<i>'goquotes-api'</i>) that fetches one random quote at a time and using kafka-python - the kafka-producer python script stores these quotes in the <i>"Quotes"</i> topic in kafka-cluster every 3 seconds.<br />
Next, I've kafka-consumer python script that's responsible for fetching these messages('quotes') from the subscribed topic: <i>"Quotes"</i> in kafka-cluster.

 
