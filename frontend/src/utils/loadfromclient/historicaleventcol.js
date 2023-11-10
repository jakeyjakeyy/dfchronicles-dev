function loadHistoricalEventCollection(object, setResponse) {
  console.log(object.getElementsByTagName("id")[0].value);
  const id = object.getElementsByTagName("id")[0].value;
  const startYear = object.getElementsByTagName("start_year")[0].value;
  const endYear = object.getElementsByTagName("end_year")[0].value;

  var eventCollections = [];
  if (object.getElementsByTagName("eventcol").length > 0) {
    object.getElementsByTagName("eventcol").forEach((eventcol) => {
      eventCollections.push(eventcol.value);
    });
  }
  var events = [];
  if (object.getElementsByTagName("event").length > 0) {
    object.getElementsByTagName("event").forEach((event) => {
      // events.push(loadHistoricalEvent(event));
      events.push(event.value);
    });
  }

  const type = object.getElementsByTagName("type")[0].value;
  const name = object.getElementsByTagName("name")[0].value;
  const isPartOfWar = object.getElementsByTagName("war_eventcol")[0].value;
  const subregion = object.getElementsByTagName("subregion_id")[0].value;
  const featureLayer = object.getElementsByTagName("feature_layer_id")[0].value;
  const site = object.getElementsByTagName("site_id")[0].value;
  // const attackers =
  // const defenders =
  // const attacking_squad_race =
  // const attacking_squad_entity =
  // const attacking_squad_number =
  // const attacking_squad_deaths =
  // const attacking_squad_site
  // const defending_squad_race =
  // const defending_squad_entity =
  // const defending_squad_number =
  // const defending_squad_deaths =
  // const defending_squad_site =
  const outcome = object.getElementsByTagName("outcome")[0].value;

  const json = {
    id: id,
    startYear: startYear,
    endYear: endYear,
    eventCollections: eventCollections,
    events: events,
    type: type,
    name: name,
    isPartOfWar: isPartOfWar,
    subregion: subregion,
    featureLayer: featureLayer,
    site: site,
    outcome: outcome,
  };
  console.log(json);
}

export default loadHistoricalEventCollection;
