function LinkSquads(object, legendsxml, legendsplusxml, type) {
  let attackingSquads = {};
  // link attacking squads
  if (object.getElementsByTagName(type + "_squad_race").length > 0) {
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
}

export default LinkSquads;
