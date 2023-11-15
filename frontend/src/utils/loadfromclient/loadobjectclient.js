import loadHistoricalEventCollection from "./historicaleventcol";

function loadObjectClient(object, legendsxml, legendsplusxml) {
  if (object.name === "historical_event_collection") {
    return loadHistoricalEventCollection(object, legendsxml, legendsplusxml);
  }
}

export default loadObjectClient;
