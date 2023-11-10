import loadHistoricalEventCollection from "./historicaleventcol";

function loadObjectClient(object, setResponse) {
  if (object.name === "historical_event_collection") {
    loadHistoricalEventCollection(object);
  }
}

export default loadObjectClient;
