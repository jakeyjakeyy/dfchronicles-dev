import loadHistoricalEvent from "./historicalevent";
import LinkSquads from "./linksquads";
import loadSubregion from "./subregion";
import getEntityData from "./entity";

function loadHistoricalEventCollection(
  object,
  setResponse,
  legendsxml,
  legendsplusxml
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

  const eventcolElements = object.getElementsByTagName("eventcol");
  if (eventcolElements.length > 0) {
    var eventCollections = [];
    eventcolElements.forEach((eventcol) => {
      legendsxml.getElementsByTagName(object.name).forEach((data) => {
        if (data.getElementsByTagName("id")[0].value === eventcol.value) {
          eventCollections.push(
            loadHistoricalEventCollection(
              data,
              setResponse,
              legendsxml,
              legendsplusxml
            )
          );
        }
      });
    });
    json.eventCollections = eventCollections;
  }

  const eventElements = object.getElementsByTagName("event");
  if (eventElements.length > 0) {
    var events = [];
    eventElements.forEach((event) => {
      events.push(loadHistoricalEvent(event.value, legendsxml, legendsplusxml));
    });
    json.events = events;
  }
  const eventTypeElements = object.getElementsByTagName("event_type");
  if (eventTypeElements.length > 0) {
    json.type = eventTypeElements[0].value;
  }
  const eventNameElements = object.getElementsByTagName("event_name");
  if (eventNameElements.length > 0) {
    json.name = eventNameElements[0].value;
  }

  const warEventColElements = object.getElementsByTagName("war_eventcol");
  if (warEventColElements.length > 0) {
    const isPartOfWar = {};
    warEventColElements.forEach((war) => {
      legendsxml
        .getElementsByTagName("historical_event_collection")
        .forEach((data) => {
          let idElements = data.getElementsByTagName("id");
          if (idElements[0].value === war.value) {
            isPartOfWar.name = data.getElementsByTagName("name")[0].value;
            isPartOfWar.id = idElements[0].value;
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

  const featurelayerElements = object.getElementsByTagName("feature_layer_id");
  if (featurelayerElements.length > 0) {
    const featureLayer = {};
    featurelayerElements.forEach((layer) => {
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

  const siteidElements = object.getElementsByTagName("site_id");
  if (siteidElements.length > 0) {
    siteidElements.forEach((site) => {
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
      }
    });
  }

  const attackinghfidElements = object.getElementsByTagName("attacking_hfid");
  if (attackinghfidElements.length > 0) {
    const attackingFigures = {};
    attackinghfidElements.forEach((attacker) => {
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

  const defendinghfidElements = object.getElementsByTagName("defending_hfid");
  if (defendinghfidElements.length > 0) {
    const defendingFigures = {};
    defendinghfidElements.forEach((defender) => {
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

  const defendingenidElements = object.getElementsByTagName("defending_enid");
  if (defendingenidElements.length > 0) {
    let enid = defendingenidElements[0].value;
    json.defenderCiv = getEntityData(enid, legendsxml, legendsplusxml);
  }
  const attackingenidElements = object.getElementsByTagName("attacking_enid");
  if (attackingenidElements.length > 0) {
    let enid = attackingenidElements[0].value;
    json.attackerCiv = getEntityData(enid, legendsxml, legendsplusxml);
  }

  return json;
}

export default loadHistoricalEventCollection;
