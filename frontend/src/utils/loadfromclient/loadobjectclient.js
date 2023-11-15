import loadHistoricalEventCollection from "./historicaleventcol";

function loadObjectClient(object, legendsxml, legendsplusxml) {
  if (!object || !object.name) {
    return {};
  }
  if (object.name === "historical_event_collection") {
    return loadHistoricalEventCollection(object, legendsxml, legendsplusxml);
  } else {
    return {};
  }
}

export default loadObjectClient;
