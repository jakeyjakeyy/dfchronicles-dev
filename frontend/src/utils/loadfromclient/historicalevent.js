import loadSubregion from "./subregion";

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
      event.subtype = data.getElementsByTagName("subtype")[0]?.value;
      if (data.getElementsByTagName("attacker_civ_id").length > 0) {
        let civid = data.getElementsByTagName("attacker_civ_id")[0].value;
        if (civid) {
          let civ = legendsplusxml.getElementsByTagName("entity")[civid];
          let civname = legendsxml.getElementsByTagName("entity")[civid];
          civname = civname.children[1]?.value;
          event.attackerCiv = {
            race: civ.children[1].value,
            type: civ.children[2].value,
            name: civname,
          };
          civid = data.getElementsByTagName("defender_civ_id")[0].value;
          civ = legendsplusxml.getElementsByTagName("entity")[civid];
          civname = legendsxml.getElementsByTagName("entity")[civid];
          console.log(civname);
          civname = civname.children[1]?.value;
          event.defenderCiv = {
            race: civ.children[1].value,
            type: civ.children[2].value,
            name: civname,
          };
        }
      }
      event.subregion = loadSubregion(data, legendsxml, legendsplusxml);
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
