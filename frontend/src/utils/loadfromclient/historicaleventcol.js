import loadHistoricalEvent from "./historicalevent";

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
  var subregion = {};
  // Link to subregion
  if (object.getElementsByTagName("subregion_id").length > 0) {
    object.getElementsByTagName("subregion_id").forEach((region) => {
      if (region.value === "-1") {
        region = undefined;
      } else {
        let obj = legendsxml.getElementsByTagName("region")[region.value];
        let subname = obj.children[1].value;
        let subtype = obj.children[2].value;
        let objplus =
          legendsplusxml.getElementsByTagName("region")[region.value];
        let evilness = objplus.children[2].value;

        subregion = {
          name: subname,
          type: subtype,
          evilness: evilness,
        };
      }
    });
  }
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
  let attackingSquads = {};
  // link attacking squads
  if (object.getElementsByTagName("attacking_squad_race").length > 0) {
    let squads = 0;
    object.getElementsByTagName("attacking_squad_race").forEach((squad) => {
      attackingSquads[squads] = { race: squad.value };
      squads++;
    });
  }
  // link entities to squad
  if (object.getElementsByTagName("attacking_squad_entity_pop").length > 0) {
    let squads = 0;
    object
      .getElementsByTagName("attacking_squad_entity_pop")
      .forEach((squad) => {
        let obj =
          legendsplusxml.getElementsByTagName("entity_population")[squad.value];
        let civ = obj.getElementsByTagName("civ_id")[0].value;
        let civname = legendsxml.getElementsByTagName("entity")[civ];
        civ = legendsplusxml.getElementsByTagName("entity")[civ];
        civname = civname.children[1].value;
        const civdict = {
          race: civ.children[1].value,
          type: civ.children[2].value,
          name: civname,
        };
        attackingSquads[squads].fromEntity = civdict;
        squads++;
      });
  }

  if (object.getElementsByTagName("attacking_squad_number").length > 0) {
    let squads = 0;
    object.getElementsByTagName("attacking_squad_number").forEach((squad) => {
      attackingSquads[squads].number = squad.value;
      squads++;
    });
  }

  if (object.getElementsByTagName("attacking_squad_deaths").length > 0) {
    let squads = 0;
    object.getElementsByTagName("attacking_squad_deaths").forEach((squad) => {
      attackingSquads[squads].deaths = squad.value;
      squads++;
    });
  }
  // link sites to squad
  if (object.getElementsByTagName("attacking_squad_site").length > 0) {
    let squads = 0;
    object.getElementsByTagName("attacking_squad_site").forEach((squad) => {
      let obj = legendsxml.getElementsByTagName("site")[squad.value];
      let subname = obj.children[2].value;
      let subtype = obj.children[1].value;
      attackingSquads[squads].fromSite = {
        name: subname,
        type: subtype,
      };
      squads++;
    });
  }
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
  if (Object.keys(attackingSquads).length > 0) {
    json.attackingSquads = attackingSquads;
  }

  if (!recursion) {
    console.log(json);
  }
  return json;
}

export default loadHistoricalEventCollection;
