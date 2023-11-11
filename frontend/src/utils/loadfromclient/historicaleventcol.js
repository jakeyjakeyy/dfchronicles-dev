import loadHistoricalEvent from "./historicalevent";

function loadHistoricalEventCollection(
  object,
  setResponse,
  legendsxml,
  legendsplusxml,
  recursion
) {
  const id = object.getElementsByTagName("id")[0]?.value;
  const startYear = object.getElementsByTagName("start_year")[0]?.value;
  const endYear = object.getElementsByTagName("end_year")[0]?.value;

  var eventCollections = [];
  if (object.getElementsByTagName("eventcol").length > 0) {
    object.getElementsByTagName("eventcol").forEach((eventcol) => {
      legendsxml.getElementsByTagName(object.name).forEach((data) => {
        if (data.getElementsByTagName("id")[0].value === eventcol.value) {
          eventCollections.push(
            loadHistoricalEventCollection(
              data,
              setResponse,
              legendsxml,
              legendsplusxml,
              true
            )
          );
        }
      });
    });
  }
  var events = [];
  if (object.getElementsByTagName("event").length > 0) {
    object.getElementsByTagName("event").forEach((event) => {
      events.push(loadHistoricalEvent(event.value, legendsxml, legendsplusxml));
    });
  }

  const type = object.getElementsByTagName("type")[0]?.value;
  const name = object.getElementsByTagName("name")[0]?.value;
  const isPartOfWar = object.getElementsByTagName("war_eventcol")[0]?.value;
  var subregion = [];
  if (object.getElementsByTagName("subregion_id").length > 0) {
    object.getElementsByTagName("subregion_id").forEach((region) => {
      if (region.value === "-1") {
        region = undefined;
      } else {
        let obj = legendsxml.getElementsByTagName("region")[region.value];
        subregion.push({
          name: obj.children[1].value,
          type: obj.children[2].value,
        });
      }
    });
  }
  const featureLayer =
    object.getElementsByTagName("feature_layer_id")[0]?.value;
  const site = object.getElementsByTagName("site_id")[0]?.value;
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
  const outcome = object.getElementsByTagName("outcome")[0]?.value;

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
  if (!recursion) {
    console.log(json);
  }
  return json;
}

export default loadHistoricalEventCollection;
