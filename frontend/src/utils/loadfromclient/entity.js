function getEntityData(civid, legendsxml, legendsplusxml) {
  let data = {};
  let civ = legendsplusxml.getElementsByTagName("entity")[civid];
  let civname = legendsxml.getElementsByTagName("entity")[civid];
  if (civname) {
    civname = civname.children[1]?.value;
    data = {
      race: civ.children[1].value,
      type: civ.children[2].value,
      name: civname,
    };
    return data;
  } else {
    return null;
  }
}

export default getEntityData;
