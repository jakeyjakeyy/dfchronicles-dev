import loadHistoricalEvent from "./historicalevent";
import LinkSquads from "./linksquads";
import loadSubregion from "./subregion";
import getEntityData from "./entity";

function loadHistoricalEventCollection(
  object,
  setResponse,
  legendsxml,
  legendsplusxml,
  recursion
) {
  const json = {};
  console.log(object);
  json.world = {
    name: legendsplusxml.children[1].value,
    dwarvishname: legendsplusxml.children[0].value,
  };
  json.id = object.getElementsByTagName("id")[0]?.value;
  json.startYear = object.getElementsByTagName("start_year")[0]?.value;
  json.endYear = object.getElementsByTagName("end_year")[0]?.value;

  // Link to other event collections
  if (object.getElementsByTagName("eventcol").length > 0) {
    var eventCollections = [];
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
    json.eventCollections = eventCollections;
  }
  // Link to other events
  if (object.getElementsByTagName("event").length > 0) {
    var events = [];
    object.getElementsByTagName("event").forEach((event) => {
      events.push(loadHistoricalEvent(event.value, legendsxml, legendsplusxml));
    });
    json.events = events;
  }

  json.type = object.getElementsByTagName("type")[0]?.value;
  json.name = object.getElementsByTagName("name")[0]?.value;
  // Link to war
  if (object.getElementsByTagName("war_eventcol").length > 0) {
    const isPartOfWar = {};
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
            let civid = data.getElementsByTagName("aggressor_ent_id")[0].value;
            isPartOfWar.agressorCivilization = getEntityData(
              civid,
              legendsxml,
              legendsplusxml
            );
            civid = data.getElementsByTagName("defender_ent_id")[0].value;
            isPartOfWar.defenderCivilization = getEntityData(
              civid,
              legendsxml,
              legendsplusxml
            );
          }
        });
    });
    json.isPartOfWar = isPartOfWar;
  }
  let subregion = loadSubregion(object, legendsxml, legendsplusxml);
  if (subregion) {
    json.subregion = subregion;
  }
  // Link to feature layer
  const featureLayer = {};
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
    json.featureLayer = featureLayer;
  }
  // Link to site
  if (object.getElementsByTagName("site_id").length > 0) {
    object.getElementsByTagName("site_id").forEach((site) => {
      if (site.value === "-1") {
        site = undefined;
      } else {
        let obj = legendsxml.getElementsByTagName("site")[site.value];
        let subname = obj.getElementsByTagName("name")[0].value;
        let subtype = obj.getElementsByTagName("type")[0].value;

        json.site = {
          name: subname,
          type: subtype,
        };
        console.log(json.site);
      }
    });
  }
  // link attackers
  if (object.getElementsByTagName("attacking_hfid").length > 0) {
    const attackingFigures = {};
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
    json.attackingFigures = attackingFigures;
  }
  // link defenders
  if (object.getElementsByTagName("defending_hfid").length > 0) {
    const defendingFigures = {};
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
    json.defendingFigures = defendingFigures;
  }
  json.attackingSquads = LinkSquads(
    object,
    legendsxml,
    legendsplusxml,
    "attacking"
  );
  json.defendingSquads = LinkSquads(
    object,
    legendsxml,
    legendsplusxml,
    "defending"
  );
  json.outcome = object.getElementsByTagName("outcome")[0]?.value;

  if (object.getElementsByTagName("defending_enid").length > 0) {
    let enid = object.getElementsByTagName("defending_enid")[0].value;
    json.defenderCiv = getEntityData(enid, legendsxml, legendsplusxml);
  }

  return json;
}

export default loadHistoricalEventCollection;
