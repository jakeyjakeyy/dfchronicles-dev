function LinkSquads(object, legendsxml, legendsplusxml, type) {
  let squadRaceTag =
    type === "attacking" ? "attacking_squad_race" : "defending_squad_race";
  let squadEntityTag =
    type === "attacking"
      ? "attacking_squad_entity_pop"
      : "defending_squad_entity_pop";
  let squadNumberTag =
    type === "attacking" ? "attacking_squad_number" : "defending_squad_number";
  let squadDeathsTag =
    type === "attacking" ? "attacking_squad_deaths" : "defending_squad_deaths";
  let squadSiteTag =
    type === "attacking" ? "attacking_squad_site" : "defending_squad_site";
  let attackingSquads = {};
  // link attacking squads
  if (object.getElementsByTagName(squadRaceTag).length > 0) {
    let squads = 0;
    object.getElementsByTagName(squadRaceTag).forEach((squad) => {
      attackingSquads[squads] = { race: squad.value };
      squads++;
    });
  }
  // link entities to squad
  if (object.getElementsByTagName(squadEntityTag).length > 0) {
    let squads = 0;
    object.getElementsByTagName(squadEntityTag).forEach((squad) => {
      let obj =
        legendsplusxml.getElementsByTagName("entity_population")[squad.value];
      if (!obj) {
        return;
      }
      let civ = obj.getElementsByTagName("civ_id")[0].value;
      let civname = legendsxml.getElementsByTagName("entity")[civ];
      civ = legendsplusxml.getElementsByTagName("entity")[civ];
      civname = civname.children[1]?.value;
      const civdict = {
        race: civ.children[1].value,
        type: civ.children[2].value,
        name: civname,
      };
      attackingSquads[squads].fromEntity = civdict;
      squads++;
    });
  }

  if (object.getElementsByTagName(squadNumberTag).length > 0) {
    let squads = 0;
    object.getElementsByTagName(squadNumberTag).forEach((squad) => {
      attackingSquads[squads].number = squad.value;
      squads++;
    });
  }

  if (object.getElementsByTagName(squadDeathsTag).length > 0) {
    let squads = 0;
    object.getElementsByTagName(squadDeathsTag).forEach((squad) => {
      attackingSquads[squads].deaths = squad.value;
      squads++;
    });
  }
  // link sites to squad
  if (object.getElementsByTagName(squadSiteTag).length > 0) {
    let squads = 0;
    object.getElementsByTagName(squadSiteTag).forEach((squad) => {
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
  return attackingSquads;
}

export default LinkSquads;
