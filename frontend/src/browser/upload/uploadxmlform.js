import React, { useEffect, useState } from "react";
import XMLParser from "react-xml-parser";

function UploadXMLForm({
  setLegendsxml,
  setLegendsPlusxml,
  onAppSelect,
  legendsxml,
  legendsplusxml,
}) {
  const [legends, setLegends] = useState(null);
  const [legendsplus, setLegendsPlus] = useState(null);

  useEffect(() => {
    if (legendsplusxml) {
      onAppSelect("Worlds");
    }
  }, [legendsplusxml]);

  const handleFormSubmit = (e) => {
    e.preventDefault();

    const reader1 = new FileReader();
    const reader2 = new FileReader();

    reader1.onload = function (event) {
      const xml1 = new XMLParser().parseFromString(event.target.result);
      reader2.onload = function (event) {
        console.log(xml1.getElementsByTagName("df_world"));
        const xml2 = new XMLParser().parseFromString(event.target.result);
        setLegendsxml(xml1);
        setLegendsPlusxml(xml2);
      };
      reader2.readAsText(legendsplus);
    };
    reader1.readAsText(legends);
  };

  return (
    <form onSubmit={handleFormSubmit}>
      <input type="file" onChange={(e) => setLegends(e.target.files[0])} />
      <input type="file" onChange={(e) => setLegendsPlus(e.target.files[0])} />
      <button type="submit">Upload and Process</button>
    </form>
  );
}

export default UploadXMLForm;
