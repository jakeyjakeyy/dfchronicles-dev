import loadHistoricalEvent from "./historicalevent";
import LinkSquads from "./linksquads";
import loadSubregion from "./subregion";

function loadHistoricalEventCollection(
  object,
  setResponse,
  legendsxml,
  legendsplusxml,
  recursion
) {
  console.log(object);
  const id = object.getElementsByTagName("id")[0]?.value;
  const startYear = object.getElementsByTagName("start_year")[0]?.value;
  const endYear = object.getElementsByTagName("end_year")[0]?.value;

  var eventCollections = [];
  // Link to other event collections
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
  // Link to other events
  if (object.getElementsByTagName("event").length > 0) {
    object.getElementsByTagName("event").forEach((event) => {
      events.push(loadHistoricalEvent(event.value, legendsxml, legendsplusxml));
    });
  }

  const type = object.getElementsByTagName("type")[0]?.value;
  const name = object.getElementsByTagName("name")[0]?.value;
  const isPartOfWar = {};
  // Link to war
  if (object.getElementsByTagName("war_eventcol").length > 0) {
    object.getElementsByTagName("war_eventcol").forEach((war) => {
      legendsxml
        .getElementsByTagName("historical_event_collection")
        .forEach((data) => {
          if (data.getElementsByTagName("id")[0].value === war.value) {
            isPartOfWar.name = data.getElementsByTagName("name")[0].value;
            isPartOfWar.id = data.getElementsByTagName("id")[0].value;
            isPartOfWar.startYear =
              data.getElementsByTagName("start_year")[0].value;
            isPartOfWar.endYear =
              data.getElementsByTagName("end_year")[0].value;
            isPartOfWar.agressorCivilization =
              data.getElementsByTagName("aggressor_ent_id")[0].value;
            isPartOfWar.defenderCivilization =
              data.getElementsByTagName("defender_ent_id")[0].value;
          }
        });
    });
  }
  var subregion = loadSubregion(object, legendsxml, legendsplusxml);
  const featureLayer = {};
  // Link to feature layer
  if (object.getElementsByTagName("feature_layer_id").length > 0) {
    object.getElementsByTagName("feature_layer_id").forEach((layer) => {
      if (layer.value === "-1") {
        layer = undefined;
      } else {
        let obj =
          legendsxml.getElementsByTagName("underground_region")[layer.value];
        let subtype = obj.children[1].value;
        let subdepth = obj.children[2].value;

        featureLayer = {
          type: subtype,
          depth: subdepth,
        };
      }
    });
  }
  const site = {};
  // Link to site
  if (object.getElementsByTagName("site_id").length > 0) {
    object.getElementsByTagName("site_id").forEach((site) => {
      if (site.value === "-1") {
        site = undefined;
      } else {
        let obj = legendsxml.getElementsByTagName("site")[site.value];
        let subname = obj.children[2].value;
        let subtype = obj.children[1].value;

        site = {
          name: subname,
          type: subtype,
        };
      }
    });
  }
  const attackingFigures = {};
  // link attackers
  if (object.getElementsByTagName("attacking_hfid").length > 0) {
    object.getElementsByTagName("attacking_hfid").forEach((attacker) => {
      let obj =
        legendsxml.getElementsByTagName("historical_figure")[attacker.value];
      let subname = obj.getElementsByTagName("name")[0].value;
      let subrace = obj.getElementsByTagName("race")[0].value;
      let subcaste = obj.getElementsByTagName("caste")[0].value;
      let birthyear = obj.getElementsByTagName("birth_year")[0].value;

      attackingFigures[attacker.value] = {
        name: subname,
        race: subrace,
        sex: subcaste,
        birthYear: birthyear,
      };
    });
  }
  const defendingFigures = {};
  // link defenders
  if (object.getElementsByTagName("defending_hfid").length > 0) {
    object.getElementsByTagName("defending_hfid").forEach((defender) => {
      let obj =
        legendsxml.getElementsByTagName("historical_figure")[defender.value];
      let subname = obj.getElementsByTagName("name")[0].value;
      let subrace = obj.getElementsByTagName("race")[0].value;
      let subcaste = obj.getElementsByTagName("caste")[0].value;
      let birthyear = obj.getElementsByTagName("birth_year")[0].value;

      defendingFigures[defender.value] = {
        name: subname,
        race: subrace,
        sex: subcaste,
        birthYear: birthyear,
      };
    });
  }
  const attackingSquads = LinkSquads(
    object,
    legendsxml,
    legendsplusxml,
    "attacking"
  );
  const defendingSquads = LinkSquads(
    object,
    legendsxml,
    legendsplusxml,
    "defending"
  );
  const outcome = object.getElementsByTagName("outcome")[0]?.value;

  const json = {
    id: id,
    startYear: startYear,
    endYear: endYear,
    eventCollections: eventCollections,
    events: events,
    type: type,
    name: name,
    subregion: subregion,
    outcome: outcome,
  };

  if (Object.keys(featureLayer).length > 0) {
    json.featureLayer = featureLayer;
  }
  if (Object.keys(isPartOfWar).length > 0) {
    json.isPartOfWar = isPartOfWar;
  }
  if (Object.keys(site).length > 0) {
    json.site = site;
  }
  if (Object.keys(attackingFigures).length > 0) {
    json.attackingFigures = attackingFigures;
  }
  if (Object.keys(defendingFigures).length > 0) {
    json.defendingFigures = defendingFigures;
  }
  if (attackingSquads && Object.keys(attackingSquads).length > 0) {
    json.attackingSquads = attackingSquads;
  }
  if (defendingSquads && Object.keys(defendingSquads).length > 0) {
    json.defendingSquads = defendingSquads;
  }

  return json;
}

export default loadHistoricalEventCollection;
