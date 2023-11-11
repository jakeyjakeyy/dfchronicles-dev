import loadHistoricalEventCollection from "./historicaleventcol";

function loadObjectClient(object, setResponse, legendsxml, legendsplusxml) {
  if (object.name === "historical_event_collection") {
    loadHistoricalEventCollection(
      object,
      setResponse,
      legendsxml,
      legendsplusxml
    );
  }
}

export default loadObjectClient;
