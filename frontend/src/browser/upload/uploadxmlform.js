import React, { useEffect, useState } from "react";
import XMLParser from "react-xml-parser";
import "./upload.css";

function UploadXMLForm({
  setLegendsxml,
  setLegendsPlusxml,
  onAppSelect,
  legendsxml,
  legendsplusxml,
}) {
  const [legends, setLegends] = useState("Browse...");
  const [legendsplus, setLegendsPlus] = useState("Browse...");

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
    <div className="UploadXMLForm">
      <div className="Header">
        <h2>Upload</h2>
      </div>
      <div className="UploadBody">
        <form className="UploadXML" onSubmit={handleFormSubmit}>
          <label>Legends</label>
          <input
            type="file"
            id="filelegends"
            style={{ display: "none" }}
            onChange={(e) => setLegends(e.target.files[0])}
          />
          <label for="filelegends" className="UploadButton">
            {legends.name ? legends.name : "Browse..."}
          </label>
          <label>Legendsplus</label>
          <input
            type="file"
            id="filelegendsplus"
            style={{ display: "none" }}
            onChange={(e) => setLegendsPlus(e.target.files[0])}
          />
          <label for="filelegendsplus" className="UploadButton">
            {legendsplus.name ? legendsplus.name : "Browse..."}
          </label>
          <button type="submit">Upload and Process</button>
        </form>
      </div>
    </div>
  );
}

export default UploadXMLForm;
