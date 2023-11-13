import React, { useState } from "react";
import "./browser.css";
import UploadXMLForm from "./upload/uploadxmlform";
import Worlds from "./worlds/worlds";
import World from "./world/world";

function Browser({ app, onAppSelect }) {
  const [id, setId] = useState(null);
  const [legendsxml, setLegendsxml] = useState(null);
  const [legendsplusxml, setLegendsPlusxml] = useState(null);

  const handleSelectId = (id) => {
    setId(id);
  };

  if (app === "Home") {
    return (
      <div className="Browser">
        <h1>Home</h1> <div>add new gens here</div>
      </div>
    );
  } else if (app === "Upload") {
    return (
      <div className="Browser">
        <UploadXMLForm
          setLegendsxml={setLegendsxml}
          setLegendsPlusxml={setLegendsPlusxml}
          onAppSelect={onAppSelect}
          legendsxml={legendsxml}
          legendsplusxml={legendsplusxml}
        />
      </div>
    );
  } else if (app === "Worlds") {
    return (
      <div className="Browser">
        <Worlds
          onAppSelect={onAppSelect}
          legendsxml={legendsxml}
          legendsplusxml={legendsplusxml}
        />
      </div>
    );
  } else if (app === "World") {
    return (
      <div className="Browser">
        <World
          id={id}
          legendsxml={legendsxml}
          legendsplusxml={legendsplusxml}
          onAppSelect={onAppSelect}
        />
      </div>
    );
  }

  // return (
  //   <div className="Browser">
  //     {app === "Home" && (
  //       <div>
  //         <h1>Home</h1> <div>add new gens here</div>
  //       </div>
  //     )}
  //     {app === "Upload" && (
  //       <UploadXMLForm
  //         setLegendsxml={setLegendsxml}
  //         setLegendsPlusxml={setLegendsPlusxml}
  //         onAppSelect={onAppSelect}
  //         legendsxml={legendsxml}
  //         legendsplusxml={legendsplusxml}
  //       />
  //     )}
  //     {app === "Worlds" && (
  //       <Worlds
  //         onAppSelect={onAppSelect}
  //         legendsxml={legendsxml}
  //         legendsplusxml={legendsplusxml}
  //       />
  //     )}
  //     {app === "World" && (
  //       <World
  //         id={id}
  //         legendsxml={legendsxml}
  //         legendsplusxml={legendsplusxml}
  //         onAppSelect={onAppSelect}
  //       />
  //     )}
  //   </div>
  // );
}

export default Browser;
