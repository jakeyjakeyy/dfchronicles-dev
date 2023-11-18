import React from "react";
import { useState, useEffect } from "react";
import "./browser.css";
import UploadXMLForm from "./upload/uploadxmlform";
import Worlds from "./worlds/worlds";
import World from "./world/world";
import Generations from "../utils/generations";
import ListItem from "./listitem";
import ViewGen from "./viewgen";
import UserPage from "./userpage/userpage";

function Browser({ app, onAppSelect }) {
  const [id, setId] = useState(null);
  const [legendsxml, setLegendsxml] = useState(null);
  const [legendsplusxml, setLegendsPlusxml] = useState(null);
  const [gens, setGens] = useState(null);
  const [currentpage, setCurrentpage] = useState(1);
  const [maxpage, setMaxpage] = useState(null);

  const handleSelectId = (id) => {
    setId(id);
  };

  useEffect(() => {
    if (app === "Home") {
      Generations("get", currentpage).then((result) => {
        setGens(result.generations);
        setMaxpage(result.maxpage);
      });
    }
  }, [app, currentpage]);

  if (app === "Home") {
    if (!gens) {
      return (
        <div className="Browser">
          <h1>Home</h1>
          <div>loading...</div>
        </div>
      );
    }
    return (
      <div className="Browser">
        <div className="Header">
          <h1>Home</h1>
        </div>
        <div className="ListItemContainer">
          {gens.map((gen) => (
            <ListItem
              key={gen.id}
              id={gen.id}
              name={gen.title}
              name2={gen.generation}
              onClick={() => {
                onAppSelect("ViewGen");
                handleSelectId(gen);
              }}
              ratings={gen.ratings}
              username={gen.user}
            />
          ))}
          {maxpage > 1 && (
            <div className="Pagination">
              <div
                className="PrevPage"
                style={
                  currentpage === 1
                    ? { pointerEvents: "none", visibility: "hidden" }
                    : {}
                }
              >
                <div
                  onClick={() => {
                    if (currentpage > 1) {
                      setCurrentpage(currentpage - 1);
                    }
                  }}
                >
                  Previous
                </div>
              </div>
              <div className="PageNumber">{currentpage}</div>
              <div
                className="NextPage"
                style={
                  currentpage > maxpage
                    ? { pointerEvents: "none", visibility: "hidden" }
                    : {}
                }
              >
                <div
                  onClick={() => {
                    if (currentpage < maxpage) {
                      setCurrentpage(currentpage + 1);
                    }
                  }}
                >
                  Next
                </div>
              </div>
            </div>
          )}
        </div>
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
  } else if (app === "ViewGen") {
    return (
      <div className="Browser">
        <ViewGen gen={id} />
      </div>
    );
  } else if (app === "User") {
    return (
      <div className="Browser">
        <UserPage onAppSelect={onAppSelect} onAppSelectId={setId} />
      </div>
    );
  }
}

export default Browser;
