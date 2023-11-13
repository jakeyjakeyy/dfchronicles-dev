import getEntityData from "./entity";

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

  const squadNumbers = object.getElementsByTagName(squadNumberTag);
  const squadDeaths = object.getElementsByTagName(squadDeathsTag);
  const squadSites = object.getElementsByTagName(squadSiteTag);
  const sites = legendsplusxml.getElementsByTagName("site");
  const squadRaces = object.getElementsByTagName(squadRaceTag);
  const squadCivs = object.getElementsByTagName(squadEntityTag);

  // Create an array with a separate object for each squad
  let attackingSquads = Array(squadNumbers.length)
    .fill(null)
    .map(() => ({}));

  for (let i = 0; i < squadNumbers.length; i++) {
    attackingSquads[i].number = squadNumbers[i].value;

    if (squadDeaths[i]) {
      attackingSquads[i].deaths = squadDeaths[i].value;
    }

    if (squadSites[i] && sites[squadSites[i].value]) {
      let obj = legendsxml.getElementsByTagName("site")[squadSites[i].value];
      let subname = obj.children[2].value;
      let subtype = obj.children[1].value;
      attackingSquads[i].fromSite = {
        name: subname,
        type: subtype,
      };
    }
    if (squadRaces[i]) {
      attackingSquads[i].race = squadRaces[i].value;
    }
    if (squadCivs[i]) {
      const fromCiv = getEntityData(
        squadCivs[i].value,
        legendsxml,
        legendsplusxml
      );
      if (fromCiv) {
        attackingSquads[i].fromCiv = fromCiv;
      } else {
        continue;
      }
    }
  }

  return attackingSquads;
}

export default LinkSquads;
