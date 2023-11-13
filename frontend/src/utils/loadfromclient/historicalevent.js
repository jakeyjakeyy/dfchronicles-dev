import loadSubregion from "./subregion";
import getEntityData from "./entity";

function loadHistoricalEvent(id, legendsxml, legendsplusxml) {
  var event = {};
  legendsxml.getElementsByTagName("historical_event").forEach((data) => {
    if (data.getElementsByTagName("id")[0].value === id) {
      console.log(data);
      event.year = data.getElementsByTagName("year")[0].value;
      event.type = data.getElementsByTagName("type")[0].value;

      if (event.type === "hf died") {
        event.type = "target died";
      }

      if (event.type === "hf wounded") {
        event.type = "target wounded";
      }

      let subtype = data.getElementsByTagName("subtype")[0]?.value;
      if (subtype) {
        event.subtype = subtype;
      }

      if (data.getElementsByTagName("attacker_civ_id").length > 0) {
        let civid = data.getElementsByTagName("attacker_civ_id")[0].value;
        if (civid) {
          event.attackerCiv = getEntityData(civid, legendsxml, legendsplusxml);
          civid = data.getElementsByTagName("defender_civ_id")[0].value;
          event.defenderCiv = getEntityData(civid, legendsxml, legendsplusxml);
        }
      }

      let subregion = loadSubregion(data, legendsxml, legendsplusxml);
      if (subregion) {
        event.subregion = subregion;
      }

      if (data.getElementsByTagName("body_part").length > 0) {
        event.bodyPart = data.getElementsByTagName("body_part")[0].value;
      }

      if (data.getElementsByTagName("death_cause").length > 0) {
        event.deathCause = data.getElementsByTagName("death_cause")[0].value;
      }

      if (data.getElementsByTagName("group_1_hfid").length > 0) {
        var involvedFigures = {};
        involvedFigures[0] = getHistoricalFigureData(
          "group_1_hfid",
          data,
          legendsxml
        );
      }
      if (data.getElementsByTagName("group_2_hfid").length > 0) {
        involvedFigures[1] = getHistoricalFigureData(
          "group_2_hfid",
          data,
          legendsxml
        );
      }
      if (involvedFigures) {
        event.involvedFigures = involvedFigures;
      }

      if (data.getElementsByTagName("attacker_general_hfid").length > 0) {
        event.attackerGeneral = getHistoricalFigureData(
          "attacker_general_hfid",
          data,
          legendsxml
        );
      }
      if (data.getElementsByTagName("defender_general_hfid").length > 0) {
        event.defenderGeneral = getHistoricalFigureData(
          "defender_general_hfid",
          data,
          legendsxml
        );
      }

      const targetTagNames = ["woundee_hfid", "hfid"];
      for (let tagName of targetTagNames) {
        if (data.getElementsByTagName(tagName).length > 0) {
          event.targetFigure = getHistoricalFigureData(
            tagName,
            data,
            legendsxml
          );
        }
      }
      const attackerTagNames = ["wounder_hfid", "slayer_hfid"];
      for (let tagName of attackerTagNames) {
        if (data.getElementsByTagName(tagName).length > 0) {
          event.attackerFigure = getHistoricalFigureData(
            tagName,
            data,
            legendsxml
          );
        }
      }

      if (data.getElementsByTagName("cause").length > 0) {
        event.cause = data.getElementsByTagName("cause")[0].value;
      }

      if (data.getElementsByTagName("civ_id").length > 0) {
        event.civ = getEntityData(
          data.getElementsByTagName("civ_id")[0].value,
          legendsxml,
          legendsplusxml
        );
        if (data.getElementsByTagName("link").length > 0) {
          event.link = data.getElementsByTagName("link")[0].value;
        }
      }
    }
  });
  return event;
}

function getHistoricalFigureData(tagName, data, legendsxml) {
  let figureData = {};
  if (data.getElementsByTagName(tagName).length > 0) {
    const hfid = data.getElementsByTagName(tagName)[0].value;
    legendsxml.getElementsByTagName("historical_figure").forEach((figure) => {
      if (figure.getElementsByTagName("id")[0].value === hfid) {
        figureData = {
          id: figure.getElementsByTagName("id")[0].value,
          name: figure.getElementsByTagName("name")[0].value,
          race: figure.getElementsByTagName("race")[0].value,
          caste: figure.getElementsByTagName("caste")[0].value,
        };
      }
    });
  }
  return figureData;
}

export default loadHistoricalEvent;
