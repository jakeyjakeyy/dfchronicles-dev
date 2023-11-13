function loadSubregion(object, legendsxml, legendsplusxml) {
  let subregion = undefined;
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

    return subregion;
  }
}

export default loadSubregion;
